import json
import os
import api_wrapper as api
import CONSTANTS
import app

# user_id = the user's index id, from 0 - num_of_students, that the user registered with.
# fb_id = facebook id, aka the 'sender_id'


# Currently, the row_id is offset by +2 of the user_id.
def _get_row_id(user_id):
    return user_id + 2

def _get_col_id(column):
    if column == "Team":
        return 1
    elif column == "id":
        return 2
    elif column == "First":
        return 3
    elif column == "Last":
        return 4
    elif column == "fid":
        return 5


def register_user(user_id, fb_id):
    row_id = _get_row_id(user_id)
    col_id = _get_col_id("fid")
    api.update_cell(CONSTANTS.SHEETS_MAP, row_id, col_id, fb_id)
    return

def is_fbid_auth_to_collect(fb_id):
    user_id = get_uid_of_fbid(fb_id)

    authorized_uids_str = os.environ['collect_ids'].split(",")
    authorized_uids = [int(uid) for uid in authorized_uids_str]

    app.log("Authorized_ids: " + str(authorized_uids))
    app.log("Your id: " + str(user_id))

    return user_id in authorized_uids


def get_uid_of_fbid(fb_id):
    sheet = api.get_db_gsheet(CONSTANTS.SHEETS_MAP)
    records = sheet.get_all_records()

    for record in records:
        if record['fid'] == fb_id:
            return record['id']





# A Wrapper class for interacting with the database