import pytest
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

from googleapilib.slides import open_presentation, parse_page
from googleapilib.slides.schema import Presentation, Page

PRESENTATION_ID = "1rXtLzSJ_kMLerdSYra3XhDQBSgpkpHA2ycd4GYLVxUM"


@pytest.fixture
def pres() -> Presentation:
    return open_presentation(PRESENTATION_ID)


def test_open_presentation(pres: Presentation):
    assert pres["presentationId"] == PRESENTATION_ID
    assert pres["slides"][0]["objectId"] == "p"
    assert (
        pres["slides"][0]["pageElements"][0]["shape"]["text"]["textElements"][1]["textRun"]["content"]
        == "{{title}}\n"
    )


def test_parse_page(pres: Presentation):
    page: Page = parse_page(PRESENTATION_ID, pres["slides"][0]["objectId"])
    assert page["objectId"] == "p"
    assert page["pageElements"][0]["shape"]["text"]["textElements"][1]["textRun"]["content"] == "{{title}}\n"
