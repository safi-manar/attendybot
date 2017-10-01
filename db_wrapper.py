import json
import os
import api_wrapper as api

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
    api.update_cell(row_id, col_id, fb_id)
    return



# A Wrapper class for interacting with the database