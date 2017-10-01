
# A list of constants string constants

# General Strings
BOT_NAME = "AttendyBot"
UNKNOWN_COMMAND = "Unknown command \"{0}\". \n For a list of available commands, type \"help\""


# Error messages
PINNED_LOCATION_ERROR = """You have attempted to share your location as a \'Pinned Location\' instead of
your true location. \n
Your attendance has NOT been recorded. Please try again using your \'Current Location\'."""
UNKNOWN_ATTACHMENT = "You have sent an attachment that {0} does not know how to deal with. Please try again".format(BOT_NAME)

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