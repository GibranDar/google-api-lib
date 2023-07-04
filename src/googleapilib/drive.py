import datetime

from .api import drive


def get_file(file_id: str):
    f = drive.files().get(fileId=file_id).execute()
    return f


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


def copy_file(file_id: str, parents: list[str], filename: str):
    f = drive.files().copy(fileId=file_id, body={"parents": parents, "name": filename}).execute()
    return f


def copy_deck(appraisal_id: str, parents: list[str], building_name: str, landlord_name: str):
    timestamp = datetime.datetime.now()
    filename = f"001_APPRAISAL - {timestamp} - {landlord_name}, {building_name}"
    appraisal = copy_file(appraisal_id, parents, filename)
    return appraisal


def copy_fimo_and_deck(
    fimo_id: str,
    appraisal_id: str,
    parents: list[str],
    building_name: str,
    landlord_name: str,
):
    """Copy proforma financial model and appraisal deck into proposal directory"""

    fimo_filename = f"000_FIMO - {landlord_name}, {building_name}"
    fimo = copy_file(fimo_id, parents, fimo_filename)
    appraisal = copy_deck(appraisal_id, parents, building_name, landlord_name)
    return fimo, appraisal
