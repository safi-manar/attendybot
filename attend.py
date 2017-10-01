import send_wrapper as send
import CONSTANTS

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