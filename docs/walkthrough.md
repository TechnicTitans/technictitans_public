# Google Drive Sync Walkthrough

## Overview
We have implemented a GitHub Action to automatically sync the latest `.llsp3` files from a Google Drive folder to `robot_code/latest`.

## Changes
- **Scripts**: Created `scripts/sync_drive.py` to handle authentication and file downloading.
- **Workflow**: Created `.github/workflows/update_from_google_drive.yml` to run the script on a schedule or manually.

## Setup Instructions
> [!IMPORTANT]
> You must configure the following GitHub Secrets for the action to work.

1.  **GDRIVE_CREDENTIALS_DATA**:
    -   Create a Google Cloud Service Account.
    -   Enable the "Google Drive API".
    -   Create a JSON key for the Service Account.
    -   Paste the entire JSON content into this secret.
    -   **Share the target Google Drive folder with the Service Account's email address.**

2.  **GDRIVE_FOLDER_ID**:
    -   Open the folder in Google Drive.
    -   Copy the ID from the URL (e.g., `.../folders/YOUR_FOLDER_ID_HERE`).
    -   Paste this ID into the secret.

## Verification
1.  Go to the **Actions** tab in your repository.
2.  Select **Update from Google Drive**.
3.  Click **Run workflow**.
4.  Wait for the job to complete.
5.  Check the `robot_code/latest` directory to see if the latest `.llsp3` file has been added.

## Troubleshooting
-   **"No .llsp3 files found"**: Ensure the folder ID is correct and the Service Account has access to the folder.
-   **Authentication Error**: Check if the JSON key is copied correctly into the secret.
