from datetime import datetime, timedelta


def diff_between_time(date_time_now, date_time_past):
    date_time_past = datetime.strptime(date_time_past, "%Y-%m-%d %H:%M:%S.%f")
    time_difference = date_time_now - date_time_past
    if time_difference > timedelta(minutes=5):
        return False
    else:
        return True