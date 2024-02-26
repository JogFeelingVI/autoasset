# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-02-23 21:29:27
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-02-26 10:28:21
import datetime

f = lambda x: ' '.join([f'{n:02}' for n in x])
dS = lambda x: f'{x:02}'

def diffdatetime(stime:datetime.datetime, etime:datetime.datetime) -> str:
    time_difference = etime - stime
    seconds = time_difference.total_seconds()

    # Convert the seconds to hours and minutes.
    day = seconds // (3600*24)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    
    time_difference_str = 'Data updated '
    # Create a human-readable string representation of the time difference.
    if day > 0:
        time_difference_str += f'{day} day{"s" if day > 1 else ""}'
    elif hours > 0:
        time_difference_str += f"{hours} hour{'s' if hours > 1 else ''}"
    elif minutes > 0:
        time_difference_str += f"{minutes} minute{'s' if minutes > 1 else ''}"
    else:
        time_difference_str = "less than a minute"
    time_difference_str += ' ago.'
    return time_difference_str

def diffnow(strtime:str) -> str:
    '''
    strtime str to datetime
    '''
    stime = datetime.datetime.strptime(strtime, '%Y-%m-%d %H:%M:%S.%f')
    return diffdatetime(stime, datetime.datetime.now())

