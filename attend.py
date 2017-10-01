import send_wrapper as send

def handle_message(sender_id, message):
    if message == "Attendance":
        message_temp = "Your attendance has been marked! (fake message)"
        send.send_message(sender_id, message_temp)
    else:
        send.send_message(sender_id, "Unknown command! Here is an echo of your message:")
        send.send_message(sender_id, message)

