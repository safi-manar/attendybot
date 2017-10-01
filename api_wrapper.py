import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import io
import os
import CONSTANTS
import time

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


# Returns a python pandas dataframe representation of the current database
def get_db_dataframe():
    client = _get_gspread_client()
    spreadsheet = client.open(CONSTANTS.SPREADSHEET_NAME)
    sheet = spreadsheet.sheet1

    sheet_bytes = sheet.export() # Export as bytes
    sheets_io = io.BytesIO(sheet_bytes) # As IOStream, readable by pandas
    df = pd.read_csv(sheets_io)
    return df

# Returns the gsheet instance of the database
def get_db_gsheet(spreadsheet_name):
    client = _get_gspread_client()
    spreadsheet = client.open(spreadsheet_name)
    gsheet = spreadsheet.sheet1
    return gsheet

# Flush a pandas dataframe to the drive spreadsheet for persistence
def flush_dataframe_to_db(df):
    client = _get_gspread_client()
    spreadsheet = client.open(CONSTANTS.SPREADSHEET_NAME)
    id = spreadsheet.id

    client.import_csv(id, df.to_csv())
    return 0


########### GSpread API ##################

def update_cell(spreadsheet_name, row, col, val):
    gsheet = get_db_gsheet(spreadsheet_name)
    gsheet.update_cell(row, col, val)
    return

def new_collect(duration):
    gsheet = get_db_gsheet(CONSTANTS.SHEETS_COLLECTIONS)
    current_time = time.time()
    records = gsheet.get_all_records()
    num_sessions = len(records)
    next_session = num_sessions + 1
    row_id = next_session + 1 # Because of the header
    start_col_id = 2
    update_cell(gsheet, row_id, start_col_id, current_time)
    return


