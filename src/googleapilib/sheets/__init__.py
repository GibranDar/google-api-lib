from dataclasses import dataclass
from pprint import pprint
from typing import Any, Literal, TypedDict, Union

from googleapilib.utilities.decorators import exponential_backoff_decorator

from googleapilib.api import sheets

# sheet types
SheetsValue = Union[str, int, float]
SheetsRange = list[list[SheetsValue]]
NamedRanges = dict[str, SheetsRange]
NamedCell = dict[str, SheetsValue]

# schemas

ValueInputOption = Literal["RAW", "USER_ENTERED"]
ValueRenderOption = Literal["FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"]
DateTimeRenderOption = Literal["SERIAL_NUMBER", "FORMATTED_STRING"]


class UpdateCellData(TypedDict):
    range: str
    values: list[list[Any]]
    majorDimension: Literal["ROWS", "COLUMNS"]


@dataclass
class BatchUpdateCellRequest:
    data: list[UpdateCellData]
    includeValuesInResponse: bool = False
    responseValueRenderOption: ValueRenderOption = "FORMATTED_VALUE"
    valueInputOption: ValueInputOption = "USER_ENTERED"


# functions


@exponential_backoff_decorator(status_code=429)
def open_workbook(spreadsheet_id: str):
    """Open a workbook."""
    workbook = sheets.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    return workbook


@exponential_backoff_decorator(status_code=429)
def get_values(spreadsheet_id: str, range: str):
    """Get values from a range in a spreadsheet."""
    res = (
        sheets.spreadsheets()
        .values()
        .get(
            spreadsheetId=spreadsheet_id,
            range=range,
            majorDimension="ROWS",
            valueRenderOption="UNFORMATTED_VALUE",
            dateTimeRenderOption="FORMATTED_STRING",
        )
        .execute()
    )
    return res["values"]


@exponential_backoff_decorator(status_code=429)
def get_charts(spreadsheet_id: str):
    """Get all charts in a spreadsheet."""
    wb = open_workbook(spreadsheet_id)
    sheets = wb["sheets"]
    charts = [sheet["charts"] for sheet in sheets if "charts" in sheet]
    return charts


@exponential_backoff_decorator(status_code=429)
def get_all_named_ranges(spreadsheet_id: str):
    """Get all named ranges from a spreadsheet."""
    wb = open_workbook(spreadsheet_id)
    named_ranges = wb.get("namedRanges", None)
    assumptions = {}
    if named_ranges:
        for named_range in named_ranges:
            assumptions[named_range["name"]] = get_values(spreadsheet_id, named_range["name"])
    return assumptions


@exponential_backoff_decorator(status_code=429)
def x_get_all_named_ranges(spreadsheet_id: str):
    wb = open_workbook(spreadsheet_id)
    named_ranges = wb.get("namedRanges", None)
    names = [named_range["name"] for named_range in named_ranges]
    res = batch_get_ranges(spreadsheet_id, names)

    assumptions = {}
    for idx, name in enumerate(names):
        assumptions[name] = res[idx]["values"]
    return assumptions


def batch_get_ranges(spreadsheet_id: str, ranges: Union[str, list[str]]):
    """Batch get ranges from a spreadsheet."""
    res = (
        sheets.spreadsheets()
        .values()
        .batchGet(
            spreadsheetId=spreadsheet_id,
            ranges=ranges,
            majorDimension="ROWS",
            valueRenderOption="UNFORMATTED_VALUE",
            dateTimeRenderOption="FORMATTED_STRING",
        )
        .execute()
    )
    return res["valueRanges"]


def batch_update(spreadsheet_id: str, body: BatchUpdateCellRequest):
    """Batch update a spreadsheet."""
    res = (
        sheets.spreadsheets()
        .values()
        .batchUpdate(spreadsheetId=spreadsheet_id, body=body.__dict__)  # type:ignore
        .execute()
    )
    return res


def append_values(spreadsheet_id: str, range: str, values: list[list[Any]]):
    """Append values to a range in a spreadsheet."""
    res = (
        sheets.spreadsheets()
        .values()
        .append(
            spreadsheetId=spreadsheet_id,
            range=range,
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body={"values": values},
        )
        .execute()
    )
    return res


def update_value(
    spreadsheet_id: str,
    row: int,
    col: int,
    value: list[Any],
    render_option: ValueRenderOption = "FORMATTED_VALUE",
    input_option: ValueInputOption = "USER_ENTERED",
):
    """Update a single row in a spreadsheet."""
    range = f"R{row}:C{col}"
    res = (
        sheets.spreadsheets()
        .values()
        .update(
            spreadsheetId=spreadsheet_id,
            range=range,
            valueInputOption=input_option,
            responseValueRenderOption=render_option,
            body={"values": [value]},
        )
        .execute()
    )
    return res
