import pytest
import random
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

from googleapilib.sheets.schema import Spreadsheet, GridRange
from googleapilib.sheets import get_values, update_value, append_values

from .test_sheets_schema import wb


def test_get_values(wb: Spreadsheet):
    sheet_title = wb["sheets"][0]["properties"]["title"]
    res = get_values(wb["spreadsheetId"], f"{sheet_title}!R1C1")
    assert res["range"] == f"{sheet_title}!A1"


def test_append_values(wb: Spreadsheet):
    sheet_title = wb["sheets"][0]["properties"]["title"]
    values = [["test", 2]]
    res = append_values(wb["spreadsheetId"], f"{sheet_title}!R1C1", values)
    assert res["spreadsheetId"] == wb["spreadsheetId"]
    assert res["updates"]["updatedRows"] == 1
    assert res["updates"]["updatedColumns"] == 2
    assert get_values(wb["spreadsheetId"], res["updates"]["updatedRange"])["values"] == values


def test_update_value(wb: Spreadsheet):
    sheet_title = wb["sheets"][0]["properties"]["title"]
    value = f"automated-{random.randint(0, 100000)}"
    res = update_value(wb["spreadsheetId"], sheet_title, "A2", [value])
    assert res["spreadsheetId"] == wb["spreadsheetId"]
    assert res["updatedRange"] == f"{sheet_title}!A2"
    assert res["updatedRows"] == 1
    assert res["updatedColumns"] == 1
    assert get_values(wb["spreadsheetId"], res["updatedRange"])["values"] == [[value]]


def test_get_named_ranges(wb: Spreadsheet):
    named_ranges = wb["namedRanges"]
    grid_range = GridRange(endColumnIndex=1, endRowIndex=1, startColumnIndex=0, startRowIndex=0, sheetId=0)  # type: ignore[misc]
    sheet_id = grid_range.pop("sheetId")
    assert len(named_ranges) == 1
    assert named_ranges[0]["name"] == "key_title"
    assert named_ranges[0]["range"] == grid_range
