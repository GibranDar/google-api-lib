from typing import TypedDict


class GoogleApiErrorResponse(TypedDict):
    code: int
    message: str
    status: str
