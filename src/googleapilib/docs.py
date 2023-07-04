from dataclasses import dataclass, asdict
from typing import Any

from .api import docs
from .utilities.decorators import exponential_backoff_decorator


@dataclass
class SubstringMatchCriteria:
    """Text references the text to search for in the Document, if match case is true the search is case sensitive"""

    text: str
    matchCase: bool = False


@dataclass
class ReplaceAllText:
    replaceText: str
    containsText: SubstringMatchCriteria


@exponential_backoff_decorator(status_code=429)
def get_document(document_id: str):
    """Open a Document"""
    doc = docs.documents().get(documentId=document_id).execute()
    return doc


@exponential_backoff_decorator(status_code=429)
def batch_update(document_id: str, requests: list[dict[str, Any]]):
    res = docs.documents().batchUpdate(documentId=document_id, body={"requests": requests}).execute()
    return res


# requests


def replace_all_text(req: ReplaceAllText):
    body = {"replaceAllText": asdict(req)}
    return body
