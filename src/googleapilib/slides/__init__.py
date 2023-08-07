from typing import Any, Optional, Literal, TypedDict, Union
from attrs import define, field, validators

from googleapilib.api import slides
from googleapilib.errors import GoogleApiErrorResponse
from googleapilib.utilities.validators import url_validator

from .schema import Presentation, Page, Table, TableCell


def open_presentation(presentation_id: str) -> Presentation:
    pres = slides.presentations().get(presentationId=presentation_id).execute()
    return Presentation(**pres)  # type: ignore[misc]


def get_page_ids(presentation) -> list[str]:
    page_ids: list[str] = []
    for page in presentation["slides"]:
        for k, v in page.items():
            if k == "objectId":
                page_ids.append(v)
    return page_ids


def parse_page(presentation_id: str, page_id: str) -> Page:
    page = slides.presentations().pages().get(presentationId=presentation_id, pageObjectId=page_id).execute()
    return Page(**page)  # type: ignore[misc]


def get_all_page_text(page: Page):
    text_objects = []
    for element in page["pageElements"]:
        if "shape" in element:
            if "text" in element["shape"]:
                text_objects.append({"id": element["objectId"], "text": element["shape"]["text"]})
    return text_objects


def get_all_page_tables(page: Page):
    table_objects = []
    for element in page["pageElements"]:
        if "table" in element:
            table_objects.append({"id": element["objectId"], "table": element["table"]})
    return table_objects


def get_table_cells(table: Table) -> list[TableCell]:
    table_rows = table["tableRows"]
    return [cell for row in table_rows for cell in row["tableCells"]]


# responses

WriteControl = TypedDict("WriteControl", {"requiredRevisionId": str})


class SlidesBatchUpdateResponse(TypedDict):
    presentationId: str
    replies: list[dict[str, Union[str, int]]]
    writeControl: WriteControl


class SlidesBatchUpdateError(TypedDict):
    error: GoogleApiErrorResponse


def batch_update(
    presentation_id: str, requests: list[Any]
) -> Union[SlidesBatchUpdateResponse, SlidesBatchUpdateError]:
    response = (
        slides.presentations()
        .batchUpdate(presentationId=presentation_id, body={"requests": requests})
        .execute()
    )

    if "error" in response:
        return SlidesBatchUpdateError(error=response["error"])
    else:
        return SlidesBatchUpdateResponse(
            presentationId=response["presentationId"],
            replies=response["replies"],
            writeControl=response["writeControl"],
        )


# requests


def split_page_ids(page_ids: str):
    page_object_ids = page_ids.split(";")
    if not page_object_ids or len(page_object_ids) == 0:
        raise ValueError("No page ID(s) provided")
    return page_object_ids


@define
class SlidesRequest:
    page_ids: str = field(validator=[validators.instance_of(str)])
    page_object_ids: list[str] = field(init=False)

    def __attrs_post_init__(self):
        self.page_object_ids = split_page_ids(self.page_ids)


@define(kw_only=True)
class ReplaceTextRequest(SlidesRequest):
    old_text: str = field(validator=[validators.instance_of(str)])
    new_text: str = field(validator=[validators.instance_of(str)])
    match_case: bool = field(default=True)


def replace_all_text(request: ReplaceTextRequest):
    """Replaces all instances of text matching a criteria with replace text.
    Replaces all instances of specified text"""

    page_object_ids = request.page_ids.split(";")
    if not page_object_ids or len(page_object_ids) == 0:
        raise ValueError("No page ID(s) provided")

    return {
        "replaceAllText": {
            "pageObjectIds": page_object_ids,
            "containsText": {"matchCase": request.match_case, "text": request.old_text},
            "replaceText": request.new_text,
        }
    }


@define(kw_only=True)
class ReplaceShapeWithImageRequest(SlidesRequest):
    old_text: str = field(validator=[validators.instance_of(str)])
    match_case: bool = field(default=True)
    replace_method: Literal["CENTER_INSIDE", "CENTER_CROP"] = field(
        default="CENTER_INSIDE",
        validator=[validators.instance_of(str), validators.in_({"CENTER_INSIDE", "CENTER_CROP"})],
    )
    image_url: Optional[str] = field(default=None, validator=[url_validator])


def replace_shape_with_image(
    request: ReplaceShapeWithImageRequest,
):
    """Replaces all shapes that match the given criteria with the provided image.
    The images replacing the shapes are rectangular after being inserted into the
    presentation and do not take on the forms of the shapes. Replaces all shapes
    matching some criteria with an image."""

    page_object_ids = request.page_ids.split(";")
    if not page_object_ids or len(page_object_ids) == 0:
        raise ValueError("No page ID(s) provided")

    return {
        "replaceAllShapesWithImage": {
            "pageObjectIds": page_object_ids,
            "containsText": {"matchCase": request.match_case, "text": request.old_text},
            "imageUrl": request.image_url,
            "imageReplaceMethod": request.replace_method,
        }
    }


@define(kw_only=True)
class ReplaceShapeWithSheetsChartRequest(SlidesRequest):
    old_text: str = field(validator=[validators.instance_of(str)])
    spreadsheet_id: str = field(validator=[validators.instance_of(str)])
    chart_id: int = field(validator=[validators.instance_of(int)])
    match_case: bool = field(default=True)
    linking_mode: Literal["LINKED", "NOT_LINKED"] = field(
        default="LINKED",
        validator=[validators.instance_of(str), validators.in_({"LINKED", "NOT_LINKED"})],
    )


def replace_shape_with_chart(request: ReplaceShapeWithSheetsChartRequest):
    return {
        "replaceAllShapesWithSheetsChart": {
            "spreadsheetId": request.spreadsheet_id,
            "chartId": request.chart_id,
            "pageObjectIds": request.page_ids,
            "containsText": {"text": request.old_text, "matchCase": request.match_case},
            "linkingMode": request.linking_mode,
        }
    }


def get_text_range(
    range_type: str = "ALL",
    start_index: Optional[int] = None,
    end_index: Optional[int] = None,
):
    RANGE_TYPE_OPTIONS = (
        ("RANGE_ALL", {"type": "ALL"}),
        (
            "FROM_START_INDEX",
            {"type": "FROM_START_INDEX", "startIndex": start_index},
        ),
        (
            "FIXED_RANGE",
            {
                "type": "FIXED_RANGE",
                "startIndex": start_index,
                "endIndex": end_index,
            },
        ),
    )

    text_range = None
    for _t, params in RANGE_TYPE_OPTIONS:
        if _t == range_type:
            text_range = params
            break
    return text_range


def insert_text_into_table_cell(table_id: str, row: int, col: int, new_text: str, insertion_index: int = 0):
    request = {
        "insertText": {
            "objectId": table_id,
            "cellLocation": {"rowIndex": row, "columnIndex": col},
            "text": new_text,
            "insertionIndex": insertion_index,
        }
    }
    return request


def delete_text_from_table_cell(
    table_id: str,
    row: int,
    col: int,
    range_type="ALL",
    start_index: Optional[int] = None,
    end_index: Optional[int] = None,
):
    request = {
        "deleteText": {
            "objectId": table_id,
            "cellLocation": {"rowIndex": row, "columnIndex": col},
            "textRange": get_text_range(range_type, start_index, end_index),
        }
    }
    return request


def edit_table_cell_text_style(
    table_id: str,
    row: int,
    col: int,
    style_obj: Any,
    fields: str,
    range_type="ALL",
    start_index: Optional[int] = None,
    end_index: Optional[int] = None,
):
    request = {
        "updateTextStyle": {
            "objectId": table_id,
            "cellLocation": {"rowIndex": row, "columnIndex": col},
            "style": style_obj,
            "textRange": get_text_range(range_type, start_index, end_index),
            "fields": fields,
        }
    }
    return request


def insert_table_row(table_id: str, row: int, col: int, insert_below=True, number=1):
    request = {
        "insertTableRows": {
            "tableObjectId": table_id,
            "cellLocation": {"rowIndex": row, "columnIndex": col},
            "insertBelow": insert_below,
            "number": number,
        }
    }
    return request


def delete_table_row(table_id: str, row: int, col: int):
    request = {
        "deleteTableRow": {
            "tableObjectId": table_id,
            "cellLocation": {"rowIndex": row, "columnIndex": col},
        }
    }
    return request
