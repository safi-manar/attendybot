import send_wrapper as send
import CONSTANTS
import os
import pandas as pd
from io import StringIO
import db_wrapper as db



# Process the data message
def process_message_event(messaging_event):
    sender_id = messaging_event["sender"]["id"]  # the facebook ID of the person sending you the message
    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
    if messaging_event["message"].get("text"):
        message_text = messaging_event["message"]["text"]  # the message's text
        # Handle the message.
        handle_message(sender_id, message_text)
    elif messaging_event["message"].get("attachments"):
        attachment_list = messaging_event["message"]["attachments"]
        handle_attachment(sender_id, attachment_list)

def handle_attachment(sender_id, attachment_list):
    attachment = attachment_list[0]
    isLocation = attachment.get("type") and attachment["type"] == "location"

    if isLocation and attachment.get("title") and attachment["title"] == "Pinned Location":
        # User sent a pinned location instead of current location
        error(sender_id, CONSTANTS.PINNED_LOCATION_ERROR)
    elif isLocation:
        send.send_message(sender_id, "You have attempted to share your current location.")
        handle_location_attendance(sender_id, attachment)
    else:
        error(sender_id, CONSTANTS.UNKNOWN_ATTACHMENT)
    return

def handle_location_attendance(sender_id, attachment):
    try:
        payload = attachment["payload"]
        coordinates = payload["coordinates"]
        lat = coordinates["lat"]
        long = coordinates["long"]
        response = "Your reported location is lat: {0} , long: {1}".format(lat, long)
        send.send_message(sender_id, response)
    except:
        error(sender_id, CONSTANTS.UNKNOWN_ERROR)


def handle_message(sender_id, message):
    message = message.lower() # Force all messages to lowercase for easier parsing
    if message == CONSTANTS.HELP:
        handle_help(sender_id, message)
    elif message == CONSTANTS.ATTENDANCE:
        handle_attendance(sender_id)
    elif message == CONSTANTS.REPORT:
        handle_report(sender_id, message)
    elif message == "register":
        handle_register_command(sender_id)
    elif message.split(" ")[0] == "register":
        handle_register(sender_id, message)
    else:
        handle_unknown(sender_id, message)

def handle_register_command(sender_id):
    users_string = unicode(os.environ['user_map'])
    users = pd.read_csv(StringIO(users_string), delimiter=",", index_col=0)
    first = users['First'].tolist()
    last = users['Last'].tolist()
    message = ""
    messages = []
    for id in range(0, len(first)):
        next_row = "{0} {1} {2}\n".format(id, first[id], last[id])
        if len(message) + len(next_row) < CONSTANTS.MESSAGE_LIMIT:
            message = message + next_row
        else:
            messages.append(message)
            message = ""
            message = message + next_row
    messages.append(message) # Append last message block

    # Construct a string:
    for message in messages:
        send.send_message(sender_id, message)
    send.send_message(sender_id, CONSTANTS.REGISTER_INFO)
    return

def handle_register(sender_id, message):
    id_str = message.split(" ")[1]
    try:
        id = int(id_str)
        users_string = unicode(os.environ['user_map'])
        users = pd.read_csv(StringIO(users_string), delimiter=",", index_col=0)

        if id > (len(users) - 1):
            send.send_message(sender_id, CONSTANTS.INVALID_ID)
            return

        first_name = users.iloc[id]['First']
        last_name = users.iloc[id]['Last']

        db.register_user(id, sender_id)

        message = "You have attempted to register as {0} {1}".format(first_name, last_name)
        send.send_message(sender_id, message)
    except:
        send.send_message(sender_id, CONSTANTS.UNKNOWN_ERROR)


def handle_attendance(sender_id):
    send.send_quick_reply_location(sender_id)
    return


def handle_help(sender_id, message):
    send.send_message(sender_id, CONSTANTS.HELP_MESSAGE)
    return

def handle_report(sender_id, message):
    send.send_message(sender_id, "PLACEHOLDER MESSAGE") #TODO
    return

def handle_unknown(sender_id, message):
    error(sender_id, CONSTANTS.UNKNOWN_COMMAND.format(message))
    return


# Send an error message
def error(sender_id, ERROR, message=""):
    if message:
        ERROR = ERROR.format(message)
    send.send_message(sender_id, ERROR)
    return