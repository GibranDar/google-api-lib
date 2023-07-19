import pytest
from dotenv import load_dotenv

load_dotenv()

from googleapilib.sheets import open_workbook
from googleapilib.sheets.schema import Spreadsheet

SPREADSHEET_ID = "1VT_1t09Dn7EOWjswM8VJWWWVlmoggI1PPze6Qe3hZp4"


@pytest.fixture
def wb() -> Spreadsheet:
    return open_workbook(SPREADSHEET_ID)


def test_open_workbook(wb: Spreadsheet):
    assert wb["spreadsheetId"] == SPREADSHEET_ID


def test_open_sheet(wb: Spreadsheet):
    sheets = wb["sheets"]
    assert sheets[0]["properties"]["sheetId"] == 0
