# pylint: disable=missing-function-docstring

import contextlib
import re
from dataclasses import dataclass
from typing import Mapping, Optional, Sequence, TypedDict

from googlemaps.client import Client
from googlemaps.exceptions import ApiError, HTTPError
from googlemaps.geocoding import geocode
from googlemaps.places import find_place, places_autocomplete

# Documentation at https://developers.google.com/maps/documentation/geocoding/requests-geocoding

LatLng = TypedDict("LatLng", {"lat": float, "lng": float})
Geometry = TypedDict("Geometry", {"location": LatLng, "viewport": Mapping[str, LatLng]})
GeoResponse = TypedDict(
    "GeoResponse",
    {"name": str, "formatted_address": str, "geometry": Geometry},
)


# geocoding schemas


@dataclass
class AddressComponent:
    long_name: str
    short_name: str
    types: list[str]


@dataclass
class PlusCode:
    compound_code: str
    global_code: str


@dataclass
class GeoCodeResponse:
    formatted_address: str
    geometry: Geometry
    name: Optional[str] = None
    address_components: Optional[list[AddressComponent]] = None
    postcode_localities: Optional[list[str]] = None
    place_id: Optional[str] = None
    plus_code: Optional[PlusCode] = None
    types: Optional[list[str]] = None

    @property
    def postcode(self) -> Optional[str]:
        """Returns postcode if long address holds a valid UK postcode"""
        if val := re.search(r"[A-z]{1,2}\d[A-z\d]? ?\d[A-z]{2}", self.formatted_address, re.IGNORECASE):
            return val.group()
        return None


@dataclass
class GeoQueryMatch:
    matches: Sequence[GeoCodeResponse]
    status: str


# autocomplete schemas

MatchedSubstring = TypedDict("MatchedSubstring", {"length": int, "offset": int})
AutocompleteTerms = TypedDict("AutocompleteTerms", {"offset": int, "value": str})


@dataclass
class StructuredFormatting:
    main_text: str
    secondary_text: str
    main_text_matched_substrings: Optional[list[MatchedSubstring]] = None
    secondary_text_matched_substrings: Optional[list[MatchedSubstring]] = None


@dataclass
class AutocompletePlace:
    description: str
    matched_substrings: MatchedSubstring
    place_id: str
    reference: str
    structured_formatting: StructuredFormatting
    terms: list[AutocompleteTerms]
    types: list[str]


# google places client


def setup_client(key: str) -> Client:
    client = Client(key=key)
    return client


@contextlib.contextmanager
def google_places_client(key: str):
    client = setup_client(key)
    yield client
    client.session.close()


# geocoding functions


def validate_postcode(postcode: str) -> bool:
    POSTCODE_REGEX = r"[A-z]{1,2}\d[A-z\d]? ?\d[A-z]{2}"  # pylint: disable=invalid-name
    if re.search(POSTCODE_REGEX, postcode, re.IGNORECASE):
        return True
    return False


def geocode_address(key: str, address: str) -> list[GeoCodeResponse]:
    with google_places_client(key) as client:
        res = geocode(
            client=client,
            address=address,
            components={"country": "GB"},
        )
    return [GeoCodeResponse(**r) for r in res]


def reverse_geocode(key: str, lat: float, lon: float):
    with google_places_client(key) as client:
        res: list[Mapping[str, str]] = client.reverse_geocode(  # type: ignore
            (lat, lon),
        )[0]
    return res


def forward_geocode_postcode(key: str, postcode: str) -> GeoCodeResponse:
    if validate_postcode(postcode) is False:
        raise ValueError(f"{postcode} is not a valid UK postcode.")

    with google_places_client(key) as client:
        res = client.geocode(  # type: ignore
            address=postcode, region="gb", components={"postal_code": postcode}
        )

    if len(res) == 0:
        raise ValueError(f"No geocoordinates found for {postcode}.")

    return GeoCodeResponse(**res[0])


def forward_geocode_query(key: str, query: str) -> GeoCodeResponse:

    with google_places_client(key) as client:
        res = find_place(
            client,
            query,
            input_type="textquery",
            fields=["formatted_address", "name", "geometry"],
        )

    if res["status"] != "OK":
        raise ValueError(f"Unable to geocode: {query} - is not a valid query.")

    best_match = res["candidates"][0]
    return GeoCodeResponse(**best_match)


# autocomplete functions


def autocomplete_search(
    key: str, query: str, session_token: Optional[str] = None
) -> Optional[list[AutocompletePlace]]:

    with google_places_client(key) as client:
        if session_token:
            client.session.headers.update({"X-Goog-Session-Token": session_token})

        try:
            predictions = places_autocomplete(
                client,
                query,
                components={"country": ["gb"]},
                session_token=session_token,
                types="geocode",
            )
        except (ApiError, HTTPError):
            return None

    if len(predictions) == 0:
        return None

    return [AutocompletePlace(**place) for place in predictions]
