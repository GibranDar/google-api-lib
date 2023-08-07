import pytest
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

from googleapilib.sheets import open_workbook, get_charts
from googleapilib.sheets.schema import Spreadsheet

SPREADSHEET_ID = "1bGvKQO9sn9TrFhYAPD5At7Fz5vWmrE9hZFiRPxPHxZQ"
SHEET_ID = 366491405


@pytest.fixture
def wb() -> Spreadsheet:
    return open_workbook(SPREADSHEET_ID)


def test_open_workbook(wb: Spreadsheet):
    assert wb["spreadsheetId"] == SPREADSHEET_ID


def test_open_sheet(wb: Spreadsheet):
    sheets = wb["sheets"]
    assert sheets[0]["properties"]["sheetId"] == SHEET_ID


def test_get_charts(wb: Spreadsheet):
    charts = get_charts(wb, SHEET_ID)
    assert len(charts) > 0
