import os
from datetime import datetime, timedelta
def generate_timestamps(start_date, end_date, interval_minutes):
    """
    Generates a list of timestamps from start_date to end_date at specified intervals!

    :param start_date: The starting date as a string in 'YYYY-MM-DD' format.
    :param end_date: The ending date as a string in 'YYYY-MM-DD' format.
    :param interval_minutes: The interval in minutes between each timestamp.
    :return: A list of timestamps as strings in 'YYYY-MM-DD HH:MM:SS' format.
    """
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    
    timestamps = []
    current = start
    
    while current <= end:
        timestamps.append(current.strftime('%Y-%m-%d %H:%M:%S'))
        current += timedelta(minutes=interval_minutes)
    
    return timestamps