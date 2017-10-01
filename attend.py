import send_wrapper as send
import CONSTANTS


# Process the data message
def process_message(messaging_event):
    sender_id = messaging_event["sender"]["id"]  # the facebook ID of the person sending you the message
    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
    if messaging_event["message"].get("text"):
        message_text = messaging_event["message"]["text"]  # the message's text
        # Handle the message.
        handle_message(sender_id, message_text)
    elif messaging_event["message"].get("attachments"):
        attachment = messaging_event["message"]["attachments"]
        handle_attachment(sender_id, attachment)

def handle_attachment(sender_id, attachment):
    send.send_message(sender_id, "You have attempted to share an attachment.")
    return

def handle_message(sender_id, message):
    if message == CONSTANTS.HELP:
        handle_help(sender_id, message)
    elif message == CONSTANTS.ATTENDANCE:
        message_temp = CONSTANTS.ATTENDANCE_CONFIRMED
        send.send_message(sender_id, message_temp)
    elif message == CONSTANTS.REPORT:
        handle_report(sender_id, message)
    else:
        handle_unknown(sender_id, message)

def handle_help(sender_id, message):
    send.send_message(sender_id, CONSTANTS.HELP_MESSAGE)
    return

def handle_report(sender_id, message):
    send.send_message(sender_id, "PLACEHOLDER MESSAGE") #TODO
    return

def handle_unknown(sender_id, message):
    response = CONSTANTS.UNKNOWN_COMMAND.format(message)
    send.send_message(sender_id, response)
    return