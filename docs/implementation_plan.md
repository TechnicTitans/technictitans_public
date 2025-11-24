# Google Drive Sync Action Plan

## Goal
Create a GitHub Action that automatically fetches the latest `.llsp` files from a Google Drive folder and commits them to `robot_code/latest` in the repository.

## User Review Required
> [!IMPORTANT]
> **Credentials**: This solution requires a Google Cloud Service Account with access to the target Google Drive folder. The Service Account JSON key must be stored as a GitHub Secret named `GDRIVE_CREDENTIALS_DATA`.
> **Folder ID**: You will need the ID of the Google Drive folder to search in. This should be stored as a secret `GDRIVE_FOLDER_ID` or hardcoded if public (not recommended).

## Proposed Changes

### Scripts
#### [NEW] [sync_drive.py](file:///scripts/sync_drive.py)
- Python script to handle the logic.
- Authenticates using `GDRIVE_CREDENTIALS_DATA` env var.
- Searches for `mimeType != 'application/vnd.google-apps.folder'` and `name contains '.llsp'`.
- Sorts by `modifiedTime` desc.
- Downloads the file to `robot_code/latest`.
- Cleans up old files in `robot_code/latest` (optional, but "latest" implies we might only want the newest). *Clarification: User said "copies the latest llsp files", plural. I will download all that match or top N? I'll assume "latest" means the single most recent version of each unique filename, or just the most recent file overall. I'll stick to "most recent file overall" or "all files modified in last X days"? Let's go with "The single most recent .llsp file" or "All .llsp files found"? The prompt says "copies the latest llsp files" (plural). I will fetch the top 5 most recent to be safe, or maybe all of them? I'll implement "fetch all .llsp files from the folder" but maybe the user means "the latest version of the project". I'll assume "latest" means "newest file" but since they said "files", I'll download the most recent file found. Actually, "latest llsp files" might mean "files that are new". I will download the single most recent file for now, or maybe all files in a specific "Latest" folder on Drive.
*Refined Plan*: I will look for the *most recent* file with `.llsp` extension. If there are multiple different projects, this might be tricky. I'll assume the user wants the single latest file. If they said "files", maybe they mean multiple. I'll add a limit, say top 1. Or maybe they mean "sync the folder". I'll assume sync the folder but only `.llsp` files.
*Correction*: "copies the latest llsp files" -> likely means "get the newest file(s)". I will implement logic to get the *single* most recent file to start, as usually "latest" implies the current state.

### Workflows
#### [NEW] [.github/workflows/update_from_google_drive.yml](file:///.github/workflows/update_from_google_drive.yml)
- Trigger: `workflow_dispatch` (manual) and `schedule` (e.g., daily/hourly).
- Steps:
    - Checkout
    - Setup Python
    - Install `google-api-python-client` `google-auth`
    - Run `scripts/sync_drive.py`
    - Check for changes
    - Commit and Push

## Verification Plan
### Automated Tests
- None possible without actual credentials during this session.
### Manual Verification
- User needs to add secrets to repo.
- Run the workflow manually.
- Check if `robot_code/latest` is populated.
