from attrs import define, field

from googleapilib.api import drive
from googleapilib.drive.schema import File, MimeType


def get_file(file_id: str) -> File:
    f = drive.files().get(fileId=file_id).execute()
    return File(**f)  # type: ignore[misc]


def get_file_field(file_id: str, field: str) -> File:
    if field not in File.__annotations__.keys():
        raise ValueError(f"Field {field} not found in File schema")
    f = drive.files().get(fileId=file_id, fields=field).execute()
    return File(**f)  # type: ignore[misc]


def copy_file(file_id: str, parents: list[str], filename: str) -> File:
    body = File(parents=parents, name=filename)
    f = drive.files().copy(fileId=file_id, body=body).execute()
    return f


# TODO: add type hints - Drive Folder


@define(kw_only=True)
class CreateFileRequest:
    name: str
    mime_type: MimeType
    parents: list[str] = field(factory=list)


def create_file(request: CreateFileRequest) -> File:
    file: File = (
        drive.files()
        .create(
            body={
                "name": request.name,
                "mimeType": request.mime_type,
                "parents": request.parents,
            }
        )
        .execute()
    )
    return file


def delete_file(file_id: str) -> None:
    return drive.files().delete(fileId=file_id).execute()


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


def get_file_list(folder_name: str, parent_id: str):
    if (
        file_results := drive.files()
        .list(
            corpora="user",
            q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and '{parent_id}' in parents",
        )
        .execute()
    ):
        return file_results


def get_or_create_file(folder_name: str, parent_id: str, request: CreateFileRequest) -> File:
    results = get_file_list(folder_name, parent_id)
    if results and len(results["files"]) == 1:
        return results["files"][0]
    return create_file(request)
