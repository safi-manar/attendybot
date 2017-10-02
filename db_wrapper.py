import json
import os
import api_wrapper as api
import CONSTANTS
import app
from datetime import datetime
# A Wrapper class for interacting with the database
# Some Labels:
#   user_id = the user's index id, from 0 - num_of_students, that the user registered with.
#   fb_id = facebook id, aka the 'sender_id'


# Currently, the row_id is offset by +2 of the user_id.
def _get_mapping_row_id(user_id):
    return user_id + 2

def _get_mapping_col_id(column):
    if column == "Team":
        return 1
    elif column == "id":
        return 2
    elif column == "First":
        return 3
    elif column == "Last":
        return 4
    elif column == "fb_id":
        return 5

# Currently, the row_id is offset by +2 of the user_id.
def _get_attendance_row_id(user_id):
    return user_id + 2

def _get_attendance_col_id(column, session_id=None):
    if column == "name_first":
        return 2
    elif column == "name_last":
        return 3
    elif column == "fb_id":
        return 4
    elif column == "session":
        return 5 + int(session_id)




def register_user(user_id, fb_id):
    row_id = _get_mapping_row_id(user_id)
    col_id = _get_mapping_col_id("fb_id")
    api.update_cell(CONSTANTS.SHEETS_MAP, row_id, col_id, fb_id)
    return

def is_fbid_auth_to_collect(fb_id):
    user_id = get_uid_of_fbid(fb_id)

    authorized_uids_str = os.environ['collect_ids'].split(",")
    authorized_uids = [int(uid) for uid in authorized_uids_str]


    return user_id in authorized_uids


def get_uid_of_fbid(fb_id):
    fb_id = int(fb_id)
    sheet = api.get_db_gsheet(CONSTANTS.SHEETS_MAP)
    records = sheet.get_all_records()
    for record in records:
        if record['fb_id'] == fb_id:
            return record['id']



def new_collect(duration=2):
    api.new_collect(duration)
    return duration


def is_session_active():
    session, start, end = api.get_most_recent_collect()
    current_time = datetime.now()
    return current_time < end


def record_attendance(fb_id, lat, long):

    user_id = get_uid_of_fbid(fb_id)
    sheet = api.get_db_gsheet(CONSTANTS.SHEETS_ATTENDANCE)
    records = sheet.get_all_records()
    user_attendance = records[user_id]

    # If the user's fb_id is not already written, do so
    if not user_attendance['fb_id']:
        row_id = _get_attendance_row_id(user_id)
        col_id = _get_attendance_col_id("fb_id")
        api.update_cell(CONSTANTS.SHEETS_ATTENDANCE, row_id, col_id, fb_id)

    # Update the database with the attendance record
    current_time = datetime.now()
    record = {}
    record['lat'] = lat
    record['long'] = long
    record['timestamp'] = str(current_time)
    record_json = json.dumps(record, sort_keys=True)

    row_id = _get_attendance_row_id(user_id)
    session_id, start, end = api.get_most_recent_collect()
    col_id = _get_attendance_col_id("session", session_id)
    api.update_cell(CONSTANTS.SHEETS_ATTENDANCE, row_id, col_id, record_json)

    return




