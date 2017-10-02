
# A list of constants and strings

# Constants
MESSAGE_LIMIT = 600
ATTENDANCE_SESSIONS_COLUMN_OFFSET = 4

# General Strings
BOT_NAME = "AttendyBot"
UNKNOWN_COMMAND = "Unknown command \"{0}\". \n For a list of available commands, type \"help\""
ATTENDANCE_REQUESTED = "Please send your current location to confirm your attendance today!"
REGISTER_INFO = "Please type in \"register #\" for the number which corresponds to your name above.\n You MUST type this number in correctly to receive attendance credit this semester!"
REGISTER_SUCCESS = "You have successfully registered as {first} {last}!"
ATTENDANCE_SUCCESS = "Success! Your attendance has been recorded!"

# Error messages
PINNED_LOCATION_ERROR = """You have attempted to share your location as a \'Pinned Location\' instead of
your true location. \n
Your attendance has NOT been recorded. Please try again using your \'Current Location\'."""
UNKNOWN_ATTACHMENT = "You have sent an attachment that {0} does not know how to deal with. Please try again".format(BOT_NAME)
UNKNOWN_ERROR = "{0} has encountered an unknown error while processing your message. Please try again, or contact a TA".format(BOT_NAME)
INVALID_ID = "You have attempted to register for an ID that does not exist. Try again."
COMMAND_UNAUTHORIZED = "You are unauthorized to use this command."
SESSION_INACTIVE = "Attendance is not being taken right now. If you were late, please contact a TA."
LOCATION_OUT_OF_RANGE = """You have attempted to record your attendance, but it seems like you are out of range of the classroom! \n
If you believe this is a mistake, contact a TA."""

# List of available Commands
ATTENDANCE = "attendance"
REPORT = "report"
HELP = "help"
REGISTER = "register"
# TA Command Panel
COLLECT = "collect"
PUBLISH = "publish"
TA = "ta"



# Special messages that AttendyBot can send to the user

HELP_MESSAGE = """Confused? Here is a list of commands you can use: \n
{attendance} - Mark your attendance \n
{report} - Show a report of your attendance for the semester \n
{register} - Register yourself in the class attendance system\n
{help} - Show the help menu \n
""".format(attendance=ATTENDANCE, report=REPORT, register=REGISTER, help=HELP)

TA_PANEL = """Hello TA! Here is a list of TA commands you can use: \n
{collect} - Begin an attendance collection session \n
{publish} - Publish the latest attendance data to the Google Drive spreadsheet \'report\' \n
{ta} - Show the TA help menu \n
""".format(collect=COLLECT, publish=PUBLISH, ta=TA)

NEW_COLLECT = "You've started a new attendance collection session. This session will expire in {duration} minutes!"
PUBLISH_SUCCESSFUL = 'The data has been successfully published to the CSV file! Check the Google Drive for the latest version'


# DB_wrapper Database Strings
SHEETS_ATTENDANCE = "attendy_data"
SHEETS_MAP = "mapping"
SHEETS_COLLECTIONS = "collections"
SHEETS_REPORT = "report"