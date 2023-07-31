from attrs import define, field, validators, asdict
from typing import Any

from googleapilib.api import docs
from googleapilib.utilities.decorators import exponential_backoff_decorator

from .schema import Document


@define(kw_only=True)
class SubstringMatchCriteria:
    """Text references the text to search for in the Document, if match case is true the search is case sensitive"""

    text: str = field(validator=validators.instance_of(str))
    matchCase: bool = field(default=False)


@define(kw_only=True)
class ReplaceAllText:
    old_text: str = field(validator=validators.instance_of(str))
    new_text: str = field(validator=validators.instance_of(str))
    match_case: bool = field(default=False)


def open_document(document_id: str) -> Document:
    """Open a Document"""
    doc = docs.documents().get(documentId=document_id).execute()
    return Document(**doc)  # type: ignore[misc]


def batch_update(document_id: str, requests: list[dict[str, Any]]):
    res = docs.documents().batchUpdate(documentId=document_id, body={"requests": requests}).execute()
    return res


# requests


def replace_all_text(req: ReplaceAllText):
    return {
        "replaceAllText": {
            "replaceText": req.new_text,
            "containsText": {"text": req.old_text, "matchCase": req.match_case},
        }
    }
