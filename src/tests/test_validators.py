import pytest
from googleapilib.utilities.validators import url_validator
from attr import make_class, attrib


@pytest.fixture
def DummyClass():
    # Set up a dummy class for testing the validator
    return make_class("DummyClass", {"url": attrib(validator=url_validator)})


def test_url_validator(DummyClass):
    valid_url = "http://www.example.com"
    instance = DummyClass(url=valid_url)
    assert instance.url == valid_url


def test_url_validator_https(DummyClass):
    valid_url = "https://www.example.com"
    instance = DummyClass(url=valid_url)
    assert instance.url == valid_url


def test_url_validator_invalid_no_scheme(DummyClass):
    invalid_url = "www.example.com"
    with pytest.raises(ValueError, match=f"{invalid_url} is not a valid URL"):
        DummyClass(url=invalid_url)


def test_url_validator_invalid_no_netloc(DummyClass):
    invalid_url = "http:///path"
    with pytest.raises(ValueError, match=f"{invalid_url} is not a valid URL"):
        DummyClass(url=invalid_url)


def test_url_validator_invalid_empty_string(DummyClass):
    with pytest.raises(ValueError, match=" is not a valid URL"):
        DummyClass(url="")


def test_url_validator_invalid_non_string(DummyClass):
    with pytest.raises(AttributeError):
        DummyClass(url=123)


def test_url_validator_invalid_none(DummyClass):
    with pytest.raises(ValueError, match="None is not a valid URL"):
        DummyClass(url=None)
