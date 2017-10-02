import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import io
import os
import CONSTANTS
import time
from datetime import datetime, timedelta
import pytz
from dateutil import parser

# Constructs a dictionary readable by oath2client ServiceAccountCredentials with key data from environment vars
def _get_keyfile_dict():
    keyfile_dict = {}
    keyfile_dict['type'] = os.environ["auth_type"]
    keyfile_dict['client_email'] = os.environ["auth_client_email"]
    keyfile_dict['private_key'] = os.environ["auth_private_key"]
    keyfile_dict['private_key_id'] = os.environ["auth_private_key_id"]
    keyfile_dict['client_id'] = os.environ["auth_client_id"]
    return keyfile_dict

# Interacts with Google Drive Gspread API
def _get_gspread_client():
    # Necessary scope for read/write
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    keyfile_dict = _get_keyfile_dict()
    creds = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_dict, scope)

    client = gspread.authorize(creds)
    return client

# Return a python pandas dataframe representation of a sheet
def get_sheet_dataframe(sheet_name):
    client = _get_gspread_client()
    spreadsheet = client.open(sheet_name)
    sheet = spreadsheet.sheet1

    sheet_bytes = sheet.export() # Export as bytes
    sheets_io = io.BytesIO(sheet_bytes) # As IOStream, readable by pandas
    df = pd.read_csv(sheets_io)
    return df

# Returns a python pandas dataframe representation of the current database
def get_db_dataframe():
    return get_sheet_dataframe(CONSTANTS.SHEETS_ATTENDANCE)

# Returns the gsheet instance of the database
def get_db_gsheet(spreadsheet_name):
    client = _get_gspread_client()
    spreadsheet = client.open(spreadsheet_name)
    gsheet = spreadsheet.sheet1
    return gsheet

# Flush a pandas dataframe to the drive spreadsheet for persistence
def flush_dataframe_to_db(df, sheet_name):
    client = _get_gspread_client()
    spreadsheet = client.open(sheet_name)
    id = spreadsheet.id

    client.import_csv(id, df.to_csv(index=False))
    return 0


########### GSpread API Calls ##################

def update_cell(spreadsheet_name, row, col, val):
    gsheet = get_db_gsheet(spreadsheet_name)
    gsheet.update_cell(row, col, val)
    return

def new_collect(duration):
    tz = pytz.timezone("US/Pacific")
    current_time = datetime.now()
    end_time = current_time + timedelta(minutes = duration)

    gsheet = get_db_gsheet(CONSTANTS.SHEETS_COLLECTIONS)
    records = gsheet.get_all_records()
    num_sessions = len(records)
    next_session = num_sessions + 1
    row_id = next_session + 1 # Because of the header
    start_col_id = 2
    end_col_id = 3
    session_col_id = 1
    # Update the session id, then start, then end time
    update_cell(CONSTANTS.SHEETS_COLLECTIONS, row_id, session_col_id, next_session)
    update_cell(CONSTANTS.SHEETS_COLLECTIONS, row_id, start_col_id, current_time)
    update_cell(CONSTANTS.SHEETS_COLLECTIONS, row_id, end_col_id, end_time)


    # next_session is now the latest session. Update the attendy_data appropriately.
    # If the column name for this session has not been written yet, do so now
    session_id = next_session
    offset = CONSTANTS.ATTENDANCE_SESSIONS_COLUMN_OFFSET
    update_cell(CONSTANTS.SHEETS_ATTENDANCE, 1, offset+int(session_id), session_id)

    return


def get_most_recent_collect():
    gsheet = get_db_gsheet(CONSTANTS.SHEETS_COLLECTIONS)
    records = gsheet.get_all_records()
    last_record = records[len(records) - 1]
    session, start, end = last_record['session'], last_record['start'], last_record['end']
    start, end = parser.parse(start), parser.parse(end)
    return session, start, end