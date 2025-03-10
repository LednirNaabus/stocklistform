import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config.config import SPREADSHEET_ID, RANGE_NAME

def get_google_sheets_service():
    creds = Credentials.from_service_account_file(
        'credentials.json', scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    service = build('sheets', 'v4', credentials=creds)
    return service

def append_to_sheet(values):
    try:
        service = get_google_sheets_service()
        body = {
            'values' : values
        }

        result = service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption='RAW',
            body=body
        ).execute()
        print(f"{result.get('updates').get('UpdatedCells')} cells appended.")
    except HttpError as e:
        print(f"{e}")