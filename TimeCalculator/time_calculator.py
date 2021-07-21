import re
import math
def add_time(start, duration, day_of = "none"):
    #convert strings into hours/mins, am/pm, day of week
    day_week = day_of.strip().lower()

    conv_list = start.strip().split(' ')
    day_time = conv_list[1]

    conv_time = conv_list[0].split(':')
    conv_hour = int(conv_time[0])
    conv_min = int(conv_time[1])


    dur_list = duration.strip().split(':')
    dur_hour = int(dur_list[0])
    dur_min = int(dur_list[1])

    #convert start hours from 12 --> 24 hours
    if day_time == 'PM':
        conv_hour = conv_hour + 12

    #convert total time
    min_hold = conv_min + dur_min
    if min_hold >= 60:
        hour_hold = conv_hour + dur_hour + 1
    else:
        hour_hold = conv_hour + dur_hour

    #convert day of week to number (sun starts week)
    day_hold = 'none'

    if day_week == 'sunday':
        day_hold = 0
    if day_week == 'monday':
        day_hold = 1
    if day_week == 'tuesday':
        day_hold = 2
    if day_week == 'wednesday':
        day_hold = 3
    if day_week == 'thursday':
        day_hold = 4
    if day_week == 'friday':
        day_hold = 5
    if day_week == 'saturday':
        day_hold = 6

    #construct future numbers
    future_hold = []
    future_days = hour_hold / 24

    future_hold.append(hour_hold)#[0] total time
    future_hold.append(hour_hold % 24) #[1]  24hr->future time,
    future_hold.append(min_hold%60)#[2] mins->#/60
    future_hold.append(future_days)#[3] how many days later
    if day_of != 'none':#[4] 0-7 days of week sun-> sat
        day_of_week = (day_hold + future_days)%7
        future_hold.append(day_of_week)
    for i in range(0,len(future_hold)):
        future_hold[i] = math.floor(future_hold[i])
        future_hold[i] = math.trunc(future_hold[i])

    #final conversion to 12 hour + remaining info of week
    new_time_arr = []
    if future_hold[1] == 0 or future_hold[1] == 12:
        new_time_arr.append('12')
    if future_hold[1] > 0 and future_hold[1] < 12:
        new_time_arr.append(str(future_hold[1]))
    if future_hold[1] > 12:
        new_time_arr.append(str(future_hold[1] - 12))
    new_time_arr.append(':')
    if future_hold[2] >=0 and future_hold[2] < 10:
        new_time_arr.append('0' + str(future_hold[2]))
    if future_hold[2] >=10 :
        new_time_arr.append(str(future_hold[2]))
    if future_hold[1] < 12:
        new_time_arr.append(' AM')
    if future_hold[1] >= 12:
        new_time_arr.append(' PM')
    if day_hold != 'none':
        if future_hold[4] == 0:
            new_time_arr.append(', Sunday')
        if future_hold[4] == 1:
            new_time_arr.append(', Monday')
        if future_hold[4] == 2:
            new_time_arr.append(', Tuesday')
        if future_hold[4] == 3:
            new_time_arr.append(', Wednesday')
        if future_hold[4] == 4:
            new_time_arr.append(', Thursday')
        if future_hold[4] == 5:
            new_time_arr.append(', Friday')
        if future_hold[4] == 6:
            new_time_arr.append(', Saturday')
    if future_hold[3] >= 1 and future_hold[3] < 2:
        new_time_arr.append(' (next day)')
    if future_hold[3] >= 2:
        new_time_arr.append(' (' + str(future_hold[3]) + ' days later)')

    #set return
    new_time = ''.join(new_time_arr)
 
    return new_time
