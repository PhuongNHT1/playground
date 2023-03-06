#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def timeConversion(s):

    # ex: s = 07:05:45PM
    # slicing the hour, minute, second & period
    hour, minute, temp = s.split(':')
    second, period = temp[0:2], temp[2:4]

    # the minute and second are the same in both clock
    # s need to convert only the hour
    hour = int(hour)
    if period == 'AM':
        if hour == 12:
            hour = hour - hour
    elif period == 'PM':
        if hour < 12:
            hour = hour + 12

    result = f'{str(hour):0>2}:{minute}:{second}'
    # concate with minutes, second
    return  result

if __name__ == '__main__':
    # s = "12:01:00PM"
    s = "12:01:00AM"
    print(timeConversion(s))
