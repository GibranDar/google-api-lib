import requests  # type:ignore

BASE_URL = "https://maps.googleapis.com/maps/api/staticmap?"


def get_map(center: str, google_api_key: str, zoom=15):
    res = requests.get(
        BASE_URL + f"center={center}&zoom={zoom}&size=445x311&key={google_api_key}"
    )
    return res


def place_map_markers(coords: list[list[float]]):

    parsable_markers: list[str] = []
    for coord in coords:

        coord_asstr = []
        for latlng in coord:
            latlng_asstr = "{:.6f}".format(latlng)
            coord_asstr.append(latlng_asstr)

        parsable_markers.append(",".join(coord_asstr))

    markers_param = ""

    # Max url length to replaceAllShapesWithImages is 2K
    for marker in parsable_markers:
        if len((markers_param + marker).encode("utf-8")) > 1024:
            break
        markers_param += f"{marker}|"

    return "&markers=size:mid|" + markers_param


def draw_map(map: bytes):
    with open("map.png", "wb") as img:
        f = img.write(map)
    return f
