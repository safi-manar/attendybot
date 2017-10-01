
# A list of constants string constants

# General Strings
BOT_NAME = "AttendyBot"
UNKNOWN_COMMAND = "Unknown command \"{0}\". \n For a list of available commands, type \"help\""
ATTENDANCE_REQUESTED = "Please send your current location to confirm your attendance today!"
ATTENDANCE_CONFIRMED = "Your attendance has been marked! (fake message)"
REGISTER_INFO = "Please type in register <#> for the number which corresponds to your name above.\n You MUST type this number in correctly to receive attendance credit this semester!"

# Error messages
PINNED_LOCATION_ERROR = """You have attempted to share your location as a \'Pinned Location\' instead of
your true location. \n
Your attendance has NOT been recorded. Please try again using your \'Current Location\'."""
UNKNOWN_ATTACHMENT = "You have sent an attachment that {0} does not know how to deal with. Please try again".format(BOT_NAME)
UNKNOWN_ERROR = "{0} has encountered an unknown error while processing your message. Please try again, or contact a TA".format(BOT_NAME)

# List of available Commands
ATTENDANCE = "attendance"
REPORT = "report"
HELP = "help"
REGISTER = "register"


# Special messages that AttendyBot can send to the user

HELP_MESSAGE = """Confused? Here are a list of commands you can use: \n
{attendance} - Mark your attendance \n
{report} - Show a report of your attendance for the semester \n
{register} - Register yourself in the class attendance system\n
{help} - Show the help menu \n
""".format(attendance=ATTENDANCE, report=REPORT, register=REGISTER, help=HELP)


# DB_wrapper Database Strings
SPREADSHEET_NAME = "attendy_data"