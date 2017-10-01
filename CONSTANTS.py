
# A list of constants string constants

# General Strings
UNKNOWN_COMMAND = "Unknown command \"{0}\". \n For a list of available commands, type \"help\""

# List of available Commands
ATTENDANCE = "attendance"
REPORT = "report"
HELP = "help"


# Messages that Attendy Bot can send to the user

ATTENDANCE_CONFIRMED = "Your attendance has been marked! (fake message)"

HELP_MESSAGE = """Confused? Here are a list of commands you can use: \n
{0} - Mark your attendance \n
{1} - Show a report of your attendance for the semester \n
{2} - Show the help menu \n
""".format(ATTENDANCE, REPORT, HELP)