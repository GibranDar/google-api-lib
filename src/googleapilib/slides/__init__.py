from pprint import pprint
from typing import Any, Optional, Literal, TypedDict, Union
from attrs import define, field, validators

from googleapilib.api import slides
from googleapilib.errors import GoogleApiErrorResponse
from googleapilib.utilities.validators import url_validator

from .schema import (
    Presentation,
    Page,
    Table,
    TableCell,
    TextRange,
    TextRangeType,
    TextContent,
)


class PageText(TypedDict):
    id: str
    text: TextContent


def open_presentation(presentation_id: str) -> Presentation:
    pres = slides.presentations().get(presentationId=presentation_id).execute()
    return Presentation(**pres)  # type: ignore[typeddict-item]


def get_page_ids(presentation) -> list[str]:
    page_ids: list[str] = []
    for page in presentation["slides"]:
        for k, v in page.items():
            if k == "objectId":
                page_ids.append(v)
    return page_ids


def parse_page(presentation_id: str, page_id: str) -> Page:
    page = (
        slides.presentations()
        .pages()
        .get(presentationId=presentation_id, pageObjectId=page_id)
        .execute()
    )
    return Page(**page)  # type: ignore[typeddict-item]


def get_all_page_text(page: Page) -> list[PageText]:
    text_objects: list[PageText] = []
    for element in page["pageElements"]:
        if "shape" in element:
            if "text" in element["shape"]:
                text_objects.append(
                    {
                        "id": element["objectId"],
                        "text": element["shape"]["text"],
                    }
                )
    return text_objects


def get_all_page_tables(page: Page) -> list[Table]:
    table_objects: list[Table] = []
    for element in page["pageElements"]:
        if table := element.get("table"):
            table_objects.append(table)
    return table_objects


def get_table_cells(table: Table) -> list[TableCell]:
    table_rows = table["tableRows"]
    return [cell for row in table_rows for cell in row["tableCells"]]


def get_text_range(
    range_type: TextRangeType = "ALL",
    start_index: Optional[int] = None,
    end_index: Optional[int] = None,
) -> TextRange:
    RANGE_TYPE_OPTIONS = (
        ("ALL", {"type": "ALL"}),
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
    return TextRange(**text_range)  # type: ignore[typeddict-item]


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
        .batchUpdate(
            presentationId=presentation_id, body={"requests": requests}
        )
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


@define(kw_only=True)
class UpdateShapeTextStyleRequest(SlidesRequest):
    object_id: str = field(validator=[validators.instance_of(str)])
    range_type: TextRangeType = field(
        default="ALL",
        validator=[
            validators.instance_of(str),
            validators.in_({"FIXED_RANGE", "FROM_START_INDEX", "ALL"}),
        ],
    )
    start_index: int = field(default=0, validator=[validators.instance_of(int)])
    end_index: Optional[int] = field(
        default=None,
        validator=validators.optional([validators.instance_of(int)]),
    )
    text_range: TextRange = field(init=False)
    style: dict[str, Union[str, int, float, bool, dict[str, Any]]] = field(
        validator=validators.deep_mapping(
            key_validator=validators.instance_of(str),
            value_validator=validators.instance_of(
                (str, int, float, bool, dict)
            ),
            mapping_validator=validators.instance_of(dict),
        )
    )
    fields: str = field(default="*")

    def __attrs_post_init__(self):
        self.text_range = get_text_range(
            self.range_type, self.start_index, self.end_index
        )


@define(kw_only=True)
class ReplaceShapeWithImageRequest(SlidesRequest):
    old_text: str = field(validator=[validators.instance_of(str)])
    match_case: bool = field(default=True)
    replace_method: Literal["CENTER_INSIDE", "CENTER_CROP"] = field(
        default="CENTER_INSIDE",
        validator=[
            validators.instance_of(str),
            validators.in_({"CENTER_INSIDE", "CENTER_CROP"}),
        ],
    )
    image_url: Optional[str] = field(default=None, validator=[url_validator])


@define(kw_only=True)
class ReplaceShapeWithSheetsChartRequest(SlidesRequest):
    old_text: str = field(validator=[validators.instance_of(str)])
    spreadsheet_id: str = field(validator=[validators.instance_of(str)])
    chart_id: int = field(validator=[validators.instance_of(int)])
    match_case: bool = field(default=True)
    linking_mode: Literal["LINKED", "NOT_LINKED"] = field(
        default="LINKED",
        validator=[
            validators.instance_of(str),
            validators.in_({"LINKED", "NOT_LINKED"}),
        ],
    )


@define(kw_only=True)
class UpdateTableCellTextRequest(SlidesRequest):
    table_id: str = field(validator=[validators.instance_of(str)])
    row: int = field(validator=[validators.instance_of(int)])
    col: int = field(validator=[validators.instance_of(int)])
    new_text: str = field(validator=[validators.instance_of(str)])
    insertion_index: int = field(
        default=0, validator=[validators.instance_of(int)]
    )


@define(kw_only=True)
class EditObjectTextStyleRequest(SlidesRequest):
    object_type: Literal["SHAPE", "TABLE"] = field(
        validator=[
            validators.instance_of(str),
            validators.in_({"SHAPE", "TABLE"}),
        ]
    )
    object_id: str = field(validator=[validators.instance_of(str)])
    row: Optional[int] = field(
        default=None,
        validator=validators.optional([validators.instance_of(int)]),
    )
    col: Optional[int] = field(
        default=None,
        validator=validators.optional([validators.instance_of(int)]),
    )
    range_type: TextRangeType = field(
        default="ALL",
        validator=[
            validators.instance_of(str),
            validators.in_({"FIXED_RANGE", "FROM_START_INDEX", "ALL"}),
        ],
    )
    start_index: int = field(default=0, validator=[validators.instance_of(int)])
    end_index: Optional[int] = field(
        default=None,
        validator=validators.optional([validators.instance_of(int)]),
    )
    text_range: TextRange = field(init=False)
    style_obj: dict[str, Union[str, int, float, bool, dict[str, Any]]] = field(
        validator=validators.deep_mapping(
            key_validator=validators.instance_of(str),
            value_validator=validators.instance_of(
                (str, int, float, bool, dict)
            ),
            mapping_validator=validators.instance_of(dict),
        )
    )
    fields: str = field(default="*")

    def __attrs_post_init__(self):
        self.text_range = get_text_range(
            self.range_type, self.start_index, self.end_index
        )


def replace_all_text(request: ReplaceTextRequest):
    """Replaces all instances of text matching a criteria with replace text.
    Replaces all instances of specified text"""

    page_object_ids = request.page_ids.split(";")
    if not page_object_ids or len(page_object_ids) == 0:
        raise ValueError("No page ID(s) provided")

    return {
        "replaceAllText": {
            "pageObjectIds": page_object_ids,
            "containsText": {
                "matchCase": request.match_case,
                "text": request.old_text,
            },
            "replaceText": request.new_text,
        }
    }


def update_shape_text_style(request: UpdateShapeTextStyleRequest):
    """Update the styling of text in a Shape or Table."""

    return {
        "updateTextStyle": {
            "objectId": request.object_id,
            "style": request.style,
            "textRange": request.text_range,
            "fields": request.fields,
        }
    }


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
            "containsText": {
                "matchCase": request.match_case,
                "text": request.old_text,
            },
            "imageUrl": request.image_url,
            "imageReplaceMethod": request.replace_method,
        }
    }


def replace_shape_with_chart(request: ReplaceShapeWithSheetsChartRequest):
    return {
        "replaceAllShapesWithSheetsChart": {
            "spreadsheetId": request.spreadsheet_id,
            "chartId": request.chart_id,
            "pageObjectIds": request.page_ids,
            "containsText": {
                "text": request.old_text,
                "matchCase": request.match_case,
            },
            "linkingMode": request.linking_mode,
        }
    }


def insert_text_into_table_cell(request: UpdateTableCellTextRequest):
    return {
        "insertText": {
            "objectId": request.table_id,
            "cellLocation": {
                "rowIndex": request.row,
                "columnIndex": request.col,
            },
            "text": request.new_text,
            "insertionIndex": request.insertion_index,
        }
    }


def edit_object_text_style(request: EditObjectTextStyleRequest):
    r = {
        "updateTextStyle": {
            "objectId": request.object_id,
            "style": request.style_obj,
            "textRange": get_text_range(
                request.range_type, request.start_index, request.end_index
            ),
            "fields": request.fields,
        }
    }
    if request.object_type == "TABLE":
        r["updateTextStyle"]["cellLocation"] = {
            "rowIndex": request.row,
            "columnIndex": request.col,
        }
    return r


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


def insert_table_row(
    table_id: str, row: int, col: int, insert_below=True, number=1
):
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


def get_object_id_of_matching_text(
    text_objs: list[PageText], match_text: str
) -> Optional[str]:
    """Returns the object ID of the first text matching the given criteria."""

    for text_obj in text_objs:
        for text in text_obj["text"]["textElements"]:
            if (
                text.get("textRun")
                and text["textRun"].get("content") == match_text
            ):
                return text_obj["id"]
    return None
