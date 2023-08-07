from pprint import pprint
from typing import Any, Literal, TypedDict, Union
from attrs import define, field, validators, asdict

from googleapilib.api import sheets
from googleapilib.utilities.decorators import exponential_backoff_decorator

from .schema import Spreadsheet, NamedRange, EmbeddedChart, Sheet, Dimension

# sheet types
SheetsValue = Union[str, int, float]
SheetsRange = list[list[SheetsValue]]
NamedRanges = dict[str, SheetsRange]
NamedCell = dict[str, SheetsValue]

# schemas

ValueInputOption = Literal["RAW", "USER_ENTERED"]
ValueRenderOption = Literal["FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"]
DateTimeRenderOption = Literal["SERIAL_NUMBER", "FORMATTED_STRING"]


class ValueRange(TypedDict):
    range: str
    values: list[list[Any]]
    majorDimension: Dimension


class UpdateValuesResponse(TypedDict):
    spreadsheetId: str
    updatedRange: str
    updatedRows: int
    updatedColumns: int
    updatedCells: int
    updatedData: ValueRange


class AppendValuesResponse(TypedDict):
    spreadsheetId: str
    tableRange: str
    updates: UpdateValuesResponse


class BatchGetValuesResponse(TypedDict):
    spreadsheetId: str
    valueRanges: list[ValueRange]


class BatchUpdateValuesResponse(TypedDict):
    valueInputOption: ValueInputOption
    data: list[ValueRange]
    includeValuesInResponse: bool
    responseValueRenderOption: ValueRenderOption
    responseDateTimeRenderOption: DateTimeRenderOption


@define(kw_only=True)
class BatchUpdateValuesRequest:
    data: list[ValueRange]
    includeValuesInResponse: bool = field(default=False)
    responseValueRenderOption: ValueRenderOption = field(default="FORMATTED_VALUE")
    valueInputOption: ValueInputOption = field(default="USER_ENTERED")


# functions


def open_workbook(spreadsheet_id: str) -> Spreadsheet:
    """Open a workbook."""
    workbook = sheets.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    return Spreadsheet(**workbook)  # type: ignore[misc]


def get_values(spreadsheet_id: str, range: str) -> ValueRange:
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
    return ValueRange(**res)  # type: ignore[misc]


def get_sheet(wb: Spreadsheet, sheet_id: int) -> Sheet:
    """Get a sheet from a workbook."""
    wb["sheets"][0]["properties"]["sheetId"]
    return [sheet for sheet in wb["sheets"] if sheet["properties"]["sheetId"] == sheet_id][0]


def get_charts(wb: Spreadsheet, sheet_id: int):
    """Get all charts within a sheet."""
    sheet = get_sheet(wb, sheet_id)
    if "charts" in sheet:
        return sheet["charts"]
    return []


def get_named_ranges(spreadsheet_id: str) -> list[NamedRange]:
    """Get all named ranges from a spreadsheet."""
    wb = open_workbook(spreadsheet_id)
    return [NamedRange(**named_range) for named_range in wb["namedRanges"]]  # type: ignore[misc]


def batch_get_ranges(spreadsheet_id: str, ranges: Union[str, list[str]]) -> BatchGetValuesResponse:
    """Batch get ranges from a spreadsheet. Ranges can be in A1 notation, R1C1 notation or reference to a named range."""
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
    return BatchGetValuesResponse(**res)  # type: ignore[misc]


def batch_update(spreadsheet_id: str, body: BatchUpdateValuesRequest) -> BatchUpdateValuesResponse:
    """Batch update a spreadsheet."""
    res = (
        sheets.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=asdict(body)).execute()
    )
    return BatchUpdateValuesResponse(**res)  # type: ignore[misc]


def append_values(spreadsheet_id: str, range: str, values: list[list[Any]]) -> AppendValuesResponse:
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
    return AppendValuesResponse(**res)  # type: ignore[misc]


def update_value(
    spreadsheet_id: str,
    sheet_title: str,
    range: str,
    value: list[Any],
    render_option: ValueRenderOption = "FORMATTED_VALUE",
    input_option: ValueInputOption = "USER_ENTERED",
) -> UpdateValuesResponse:
    """Update a single row in a spreadsheet."""
    res = (
        sheets.spreadsheets()
        .values()
        .update(
            spreadsheetId=spreadsheet_id,
            range=f"{sheet_title}!{range}",
            valueInputOption=input_option,
            responseValueRenderOption=render_option,
            body={"values": [value]},
        )
        .execute()
    )
    return UpdateValuesResponse(**res)  # type: ignore[misc]
