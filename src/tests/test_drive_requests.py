import pytest
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

from googleapilib.drive import get_file, copy_file


@pytest.fixture
def file_id() -> str:
    return "1rXtLzSJ_kMLerdSYra3XhDQBSgpkpHA2ycd4GYLVxUM"


def test_get_file(file_id: str):
    f = get_file(file_id)
    assert f["id"] == file_id


def test_copy_file(file_id: str):
    f = copy_file(file_id, parents=["1E54B6cwSMCdphT63ngFow9xwtkSf_nUA"], filename="test")
    assert f["id"] != file_id
    assert f["name"] == "test"
