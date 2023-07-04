from urllib.parse import urlparse


def url_validator(instance, attribute, value):
    parsed = urlparse(value)
    if not all([parsed.scheme, parsed.netloc]):
        raise ValueError(f"{value} is not a valid URL")
