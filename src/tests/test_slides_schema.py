from dotenv import load_dotenv

load_dotenv()

import pytest
from pprint import pprint

from googleapilib.slides import open_presentation
from googleapilib.slides.schema import Presentation


@pytest.fixture
def presentation_id() -> str:
    return "1rXtLzSJ_kMLerdSYra3XhDQBSgpkpHA2ycd4GYLVxUM"


def test_open_presentation(presentation_id: str):
    pres: Presentation = open_presentation(presentation_id)
    assert pres["presentationId"] == presentation_id
    assert pres["slides"][0]["objectId"] == "p"
    assert (
        pres["slides"][0]["pageElements"][0]["shape"]["text"]["textElements"][1]["textRun"]["content"]
        == "{{title}}\n"
    )
