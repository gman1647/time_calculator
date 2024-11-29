"""
Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.
"""

new_time = {"hour": "", "minute": "","meridian":""}

def add_time(start, duration):
    start_dict = split_time(start)
    duration = split_time(duration)
    mins_start = time_to_mins(start_dict)
    mins_dur = time_to_mins(duration)
    mer = start_dict["meridian"]
    if mer == "PM":
        mins_start = mins_start + 720
    total_mins = mins_dur + mins_start
    ret_days = make_days(total_mins)
    ret_hours = make_hours(total_mins)
    ret_min = make_minutes(total_mins)
    ret_mer = make_mer(total_mins)
    print(f'The time is now {ret_hours}:{ret_min} {ret_mer}{ret_days}')
    return str(ret_hours) + ':' + str(ret_min) + ' ' + ret_mer + ret_days

def split_time(time):
    hour = time.split(":").pop(0)
    minute = time.split(" ")[0].split(":").pop()
    meridian = ""
    if time.split(" ")[0] == time:
        return({"hour": hour, "minute": minute})
    else:
        meridian = time.rsplit(" ").pop()
        return({"hour": hour, "minute": minute, "meridian": meridian})

def make_mer(min):
    hours = min // 60
    if (hours // 12) % 2 == 0:
        mer = "AM"
    else: mer = "PM"
    return mer

def time_to_mins(dict):
    time = int(dict["hour"]) * 60 + int(dict["minute"])
    return time

def make_minutes(minutes):
    if minutes > 59:
        minutes = minutes % 60
    else:
         minutes = minutes
    if minutes < 10:
        minutes = "0" + str(minutes)
    return minutes

def make_hours(min):
    if min > 59:
        hours = min // 60
    if hours >= 24:
        if hours % 12 == 0:
            hours = 12
        else: 
            hours = hours % 24
    elif hours > 13:
        hours = hours - 12
    return hours

def make_days(min):
    days = ""
    days = min // 1440
    if days > 1:
        days = " (" + str(days) + " days later)"
    elif days == 1:
        days = " (next day)"
    else:
        days = ""
    return(days)

add_time('3:30 PM', '2:12') #should return '5:42 PM'.
add_time('11:55 AM', '3:12') #should return '3:07 PM'.
add_time('2:59 AM', '24:00') #should return '2:59 AM (next day)'.
add_time('11:59 PM', '24:05') # should return '12:04 AM (2 days later)'.
add_time('8:16 PM', '466:02') # should return '6:18 AM (20 days later)'.
# # add_time('3:30 PM', '2:12', 'Monday') #should return '5:42 PM, Monday'.
# add_time('2:59 AM', '24:00', 'saturDay') #should return '2:59 AM, Sunday (next day)'.
# add_time('11:59 PM', '24:05', 'Wednesday') #should return '12:04 AM, Friday (2 days later)'.
# add_time('8:16 PM', '466:02', 'tuesday') #should return '6:18 AM, Monday (20 days later)'.
#Waiting:3. Expected time to end with '(next day)' when it is the next day.
#Waiting:4. Expected period to change from AM to PM at 12:00.
#Waiting:8. Expected adding 0:00 to return the initial time.

# add_time('3:30 PM', '2:12') #, 'Monday') #should return '5:42 PM, Monday'.
# add_time('2:59 AM', '24:00')#, 'saturDay') #should return '2:59 AM, Sunday (next day)'.
# add_time('11:59 PM', '24:05')#, 'Wednesday') #should return '12:04 AM, Friday (2 days later)'.
# add_time('8:16 PM', '466:02')




    # hours = int(start_dict["hour"]) + int(duration["hour"])
    # minutes = int(start_dict["minute"]) + int(duration["minute"])
    # minutes = int(minutes) + (int(hours) * 60)
    # print(minutes)
    # days = day_checker(start_dict["hour"], duration["hour"], start_dict["meridian"])
    # mer = start_dict["meridian"]
    # if minutes > 59:
    #     hours = hours + (minutes // 60)
    #     minutes = minutes % 60
    #     if minutes < 10:
    #         minutes = "0" + str(minutes)
    #     if hours // 12 % 2 != 0:
    #         mer = meridian_cycle(mer)
    # if hours > 24:
    #     hours = hours - (24 * days)
    # elif hours > 12:
    #     hours = hours -12
    # else:
    #     pass
    # if days == 0:
    #     days = ""
    # elif days == 1:
    #     days = " (next day)"
    # else:
    #     days = "(" + str(days) + " days later)"