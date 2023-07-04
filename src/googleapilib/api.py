import os

from google.auth.exceptions import DefaultCredentialsError
from googleapiclient.discovery import build

try:
    drive = build("drive", "v3")
    sheets = build("sheets", "v4")
    slides = build("slides", "v1")
    docs = build("docs", "v1")

except DefaultCredentialsError as e:
    from google.oauth2.service_account import Credentials

    creds = Credentials.from_service_account_file(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

    drive = build("drive", "v3", credentials=creds)
    sheets = build("sheets", "v4", credentials=creds)
    slides = build("slides", "v1", credentials=creds)
    docs = build("docs", "v1", credentials=creds)
