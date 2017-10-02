import pandas as pd
from datetime import datetime
from dateutil import parser
import api_wrapper as api
import CONSTANTS
import app


# Given a dataframe representation of the attendy_data.csv database, this script will
#   generate a clean report of attendance per student per day.

def publish(db):
    collections = api.get_sheet_dataframe(CONSTANTS.SHEETS_COLLECTIONS)
    session_to_days, days_to_session = get_session_maps(collections)
    report = construct_report_df(db, session_to_days, days_to_session)
    return report


# Given a datetime as a string, return the fixed class time date representation
def fix_class_time(start):
    app.log("Trying to parse: " + str(start))
    date = parser.parse(start)
    fixed = datetime(date.year, date.month, date.day, 14, 0, 0) # Class starts at 2PM
    return fixed


def get_session_maps(collections):
    session_to_days = {}
    days_to_session = {}

    for i in range(len(collections)):
        session_id = collections.iloc[i]['session']
        class_day = fix_class_time(collections.iloc[i]['start'])
        session_to_days[session_id] = class_day

        if class_day not in days_to_session:
            sessions = [session_id]
            days_to_session[class_day] = sessions
        else:
            # Update the current map
            sessions = days_to_session[class_day]
            sessions.append(session_id)
            days_to_session[class_day] = sessions


    return session_to_days, days_to_session

def construct_report_df(db, session_to_days, days_to_session):
    report = db.copy()
    report['total_absences'] = [0 for i in range(len(report))]

    # For each day
    for day in sorted(list(days_to_session.keys())):
        sessions = days_to_session[day]
        # For each user
        for id in range(len(db)):
            attended = True
            for session in sessions:
                # print(str(id))
                # print(str(session))
                session_attendance = db.loc[id, str(session)]
                attended = attended and bool(session_attendance == session_attendance)

            # Update total_absence count and record for this day
            if attended:
                report.loc[id, day] = "Yes"
            else:
                report.loc[id, day] = "No"
                report.loc[id, 'total_absences'] = report.loc[id, 'total_absences'] + 1

    # Clean up columns in attend
    for session in sorted(list(session_to_days.keys())):
        del report[str(session)]
    del report["fb_id"]

    return report