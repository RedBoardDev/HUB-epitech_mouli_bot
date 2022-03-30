import datetime

def set_timezone_date(date_str: str):
    date_time_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M')
    date_time_obj = date_time_obj.replace(tzinfo=datetime.timezone.utc)
    date_time_obj = date_time_obj.astimezone(datetime.timezone(datetime.timedelta(hours=+1)))
    date_time_obj = date_time_obj.replace(tzinfo=None)
    return (date_time_obj.strftime('%d/%m/%Y %H:%M'))

def set_format_date(date_str: str):
    date_time_obj = datetime.datetime.strptime(date_str, '%H:%M:%S %Y-%m-%d')
    return (date_time_obj.strftime('%d/%m/%Y %H:%M'))
