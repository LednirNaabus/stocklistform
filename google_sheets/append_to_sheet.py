from googleapiclient.errors import HttpError
from config.config import SPREADSHEET_ID, RANGE_NAME
from google_sheets.google_sheets_service import get_google_sheets_service

def append_to_sheet(values: list):
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
        print(f"{result.get('updates').get('UpdatedCeclls')} cells appended.")
    except HttpError as e:
        print(f"{e}")