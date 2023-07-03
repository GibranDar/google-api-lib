from typing import Any, Optional

from .api import slides


def open_presentation(presentation_id: str):
    pres = slides.presentations().get(presentationId=presentation_id).execute()
    return pres


def get_page_ids(presentation):
    page_ids: list[str] = []
    for page in presentation["slides"]:
        for k, v in page.items():
            if k == "objectId":
                page_ids.append(v)
    return page_ids


def parse_page(presentation_id: str, page_id: str):
    page = (
        slides.presentations()
        .pages()
        .get(presentationId=presentation_id, pageObjectId=page_id)
        .execute()
    )
    return page


def get_all_page_text(page):
    text_objects = []
    for element in page["pageElements"]:
        if "shape" in element:
            if "text" in element["shape"]:
                text_objects.append(
                    {"id": element["objectId"], "text": element["shape"]["text"]}
                )
    return text_objects


def get_all_page_tables(page):
    table_objects = []
    for element in page["pageElements"]:
        if "table" in element:
            table_objects.append({"id": element["objectId"], "table": element["table"]})
    return table_objects


def get_table_cells(table):
    table_rows = table["table"]["tableRows"]

    cells = []
    for row in table_rows:
        table_cells = row["tableCells"]
        for cell in table_cells:
            cells.append(cell)

    return cells


def batch_update(presentation_id: str, requests: list[Any]):
    response = (
        slides.presentations()
        .batchUpdate(presentationId=presentation_id, body={"requests": requests})
        .execute()
    )
    return response


# requests


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


def insert_text_into_table_cell(
    table_id: str, row: int, col: int, new_text: str, insertion_index: int = 0
):
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


def replace_all_text(
    page_ids: list[str], old_text: str, new_text: str, match_case=True
):
    request = {
        "replaceAllText": {
            "pageObjectIds": page_ids,
            "containsText": {"matchCase": match_case, "text": old_text},
            "replaceText": new_text,
        }
    }
    return request


def replace_shape_with_chart(
    spreadsheet_id: str,
    chart_id: int,
    page_ids: list[str],
    match_text: str,
    match_case=True,
    linking_mode="LINKED",
):
    request = {
        "replaceAllShapesWithSheetsChart": {
            "spreadsheetId": spreadsheet_id,
            "chartId": chart_id,
            "pageObjectIds": page_ids,
            "containsText": {"text": match_text, "matchCase": match_case},
            "linkingMode": linking_mode,
        }
    }
    return request


def replace_shape_with_image(
    image_url: str,
    page_ids: list[str],
    match_text: str,
    match_case=True,
    replace_method="CENTER_INSIDE",
):
    request = {
        "replaceAllShapesWithImage": {
            "pageObjectIds": page_ids,
            "containsText": {"matchCase": match_case, "text": match_text},
            "imageUrl": image_url,
            "imageReplaceMethod": replace_method,
        }
    }
    return request
