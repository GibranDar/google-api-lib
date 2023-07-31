import datetime

from googleapilib.api import drive
from googleapilib.drive.schema import File


def get_file(file_id: str) -> File:
    f = drive.files().get(fileId=file_id).execute()
    return File(**f)  # type: ignore[misc]


def copy_file(file_id: str, parents: list[str], filename: str) -> File:
    body = File(parents=parents, name=filename)
    f = drive.files().copy(fileId=file_id, body=body).execute()
    return f


# TODO: add type hints - Drive Folder


def create_folder(folder_name: str, parents: list[str] = []):
    folder_created = (
        drive.files()
        .create(
            body={
                "name": folder_name,
                "mimeType": "application/vnd.google-apps.folder",
                "parents": parents,
            }
        )
        .execute()
    )
    return folder_created


def list_items_in_directory(parent_id: str):
    if (
        file_results := drive.files()
        .list(
            corpora="user",
            q=f"'{parent_id}' in parents",
        )
        .execute()
    ):
        return file_results


def get_folder_list(folder_name: str, parent_id: str):
    if (
        file_results := drive.files()
        .list(
            corpora="user",
            q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and '{parent_id}' in parents",
        )
        .execute()
    ):
        return file_results


def get_or_create_folder(folder_name: str, parent_id: str):
    results = get_folder_list(folder_name, parent_id)
    if results and len(results["files"]) == 1:
        folder = results["files"][0]
    else:
        folder = create_folder(folder_name, parents=[parent_id])
    return folder
