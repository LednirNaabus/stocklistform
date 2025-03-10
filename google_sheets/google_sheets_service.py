from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build, Resource
from config.config import SPREADSHEET_ID, RANGE_NAME

def get_google_sheets_service() -> Resource:
    creds = Credentials.from_service_account_file(
        'credentials.json', scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    service = build('sheets', 'v4', credentials=creds)
    return service