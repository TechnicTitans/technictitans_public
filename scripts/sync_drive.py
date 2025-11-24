import os
import io
import json
import shutil
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# Configuration
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
# Expecting the service account JSON in this environment variable
SERVICE_ACCOUNT_INFO_VAR = 'GDRIVE_CREDENTIALS_DATA'
# Expecting the folder ID in this environment variable
FOLDER_ID_VAR = 'GDRIVE_FOLDER_ID'
TARGET_DIR = 'robot_code/latest'

def authenticate():
    creds_json = os.environ.get(SERVICE_ACCOUNT_INFO_VAR)
    if not creds_json:
        raise ValueError(f"Environment variable {SERVICE_ACCOUNT_INFO_VAR} not found.")
    
    try:
        creds_dict = json.loads(creds_json)
        creds = service_account.Credentials.from_service_account_info(
            creds_dict, scopes=SCOPES)
        return creds
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in {SERVICE_ACCOUNT_INFO_VAR}.")

def get_latest_llsp_file(service, folder_id):
    # Query for .llsp files in the specific folder, not trashed
    query = (
        f"'{folder_id}' in parents and "
        "mimeType != 'application/vnd.google-apps.folder' and "
        "name contains '.llsp3' and "
        "trashed = false"
    )
    
    # Get the latest modified file
    results = service.files().list(
        q=query,
        orderBy='modifiedTime desc',
        pageSize=1,
        fields="files(id, name, modifiedTime)"
    ).execute()
    
    files = results.get('files', [])
    if not files:
        print("No .llsp3 files found.")
        return None
    
    return files[0]

def download_file(service, file_id, file_name, target_dir):
    request = service.files().get_media(fileId=file_id)
    target_path = os.path.join(target_dir, file_name)
    
    print(f"Downloading {file_name} to {target_path}...")
    
    with io.FileIO(target_path, 'wb') as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%.")
    
    print("Download complete.")

def clean_target_directory(target_dir):
    """Removes existing .llsp files in the target directory to ensure only the latest exists."""
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        return

    for item in os.listdir(target_dir):
        if item.endswith(".llsp3"):
            os.remove(os.path.join(target_dir, item))
            print(f"Removed old file: {item}")

def main():
    folder_id = os.environ.get(FOLDER_ID_VAR)
    if not folder_id:
        raise ValueError(f"Environment variable {FOLDER_ID_VAR} not found.")
    
    print("Authenticating...")
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    
    print(f"Checking for latest .llsp3 file in folder {folder_id}...")
    latest_file = get_latest_llsp_file(service, folder_id)
    
    if latest_file:
        print(f"Found latest file: {latest_file['name']} (ID: {latest_file['id']})")
        
        # Ensure target directory exists and is clean
        clean_target_directory(TARGET_DIR)
        
        # Download
        download_file(service, latest_file['id'], latest_file['name'], TARGET_DIR)
    else:
        print("No files to sync.")

if __name__ == '__main__':
    main()
