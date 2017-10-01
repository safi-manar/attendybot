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
        send.send_message(sender_id, "Unknown command! Here is an echo of your message:")
        send.send_message(sender_id, message)

def handle_help(sender_id, message):
    send.send_message(sender_id, CONSTANTS.HELP_MESSAGE)
    return

def handle_report(sender_id, message):
    send.send_message(sender_id, "PLACEHOLDER MESSAGE") #TODO
    return