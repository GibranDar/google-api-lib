# type: ignore

import pytest
from dotenv import load_dotenv

load_dotenv()

from googleapilib.slides import (
    ReplaceTextRequest,
    replace_all_text,
    ReplaceShapeWithImageRequest,
    replace_shape_with_image,
)


def test_replace_all_text():
    request = ReplaceTextRequest(old_text="old", new_text="new", match_case=True)
    page_ids = ["page1", "page2"]

    result = replace_all_text(page_ids, request)

    expected = {
        "replaceAllText": {
            "pageObjectIds": page_ids,
            "containsText": {"matchCase": request.match_case, "text": request.old_text},
            "replaceText": request.new_text,
        }
    }
    assert result == expected


def test_replace_all_text_no_page_ids():
    request = ReplaceTextRequest(old_text="old", new_text="new", match_case=True)

    with pytest.raises(ValueError):
        replace_all_text([], request)


def test_replace_shape_with_image():
    request = ReplaceShapeWithImageRequest(
        image_url="http://test.com", match_text="match", match_case=True, replace_method="CENTER_INSIDE"
    )
    page_ids = ["page1", "page2"]

    result = replace_shape_with_image(page_ids, request)

    expected = {
        "replaceAllShapesWithImage": {
            "pageObjectIds": page_ids,
            "containsText": {"matchCase": request.match_case, "text": request.match_text},
            "imageUrl": request.image_url,
            "imageReplaceMethod": request.replace_method,
        }
    }
    assert result == expected


def test_replace_shape_with_image_no_page_ids():
    request = ReplaceShapeWithImageRequest(
        image_url="http://test.com", match_text="match", match_case=True, replace_method="CENTER_INSIDE"
    )

    with pytest.raises(ValueError):
        replace_shape_with_image([], request)


def test_replace_text_request_invalid_type():
    with pytest.raises(TypeError):
        ReplaceTextRequest(old_text=123, new_text="new", match_case=True)


def test_replace_shape_with_image_request_invalid_url():
    with pytest.raises(ValueError):
        ReplaceShapeWithImageRequest(
            image_url="invalid url", match_text="match", match_case=True, replace_method="CENTER_INSIDE"
        )


def test_replace_shape_with_image_invalid_replace_method():
    with pytest.raises(ValueError):
        ReplaceShapeWithImageRequest(
            image_url="http://test.com", match_text="match", match_case=True, replace_method="INVALID"
        )


def test_replace_all_text_null_string():
    with pytest.raises(TypeError):
        ReplaceTextRequest(old_text=None, new_text="new", match_case=True)


def test_replace_shape_with_image_null_string():
    with pytest.raises(TypeError):
        ReplaceShapeWithImageRequest(
            image_url="http://test.com", match_text=None, match_case=True, replace_method="CENTER_INSIDE"
        )
