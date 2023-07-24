import pytest
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

from googleapilib.docs import open_document
from googleapilib.docs.schema import Document

DOCUMENT_ID = "16CDyOuoQrVCgJSuXIM0DUgh70_e0dKiraD6i4Lmu_NQ"


@pytest.fixture
def document() -> Document:
    return open_document(DOCUMENT_ID)


def test_open_document(document: Document):
    assert document["documentId"] == DOCUMENT_ID
    pprint(
        document["body"]["content"],
        width=200,
        indent=2,
        sort_dicts=False,
    )
