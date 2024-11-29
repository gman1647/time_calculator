"""
Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.
"""
days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#Main function that given a time, duration, and optional day will return the time and day (if required) once the duration has elapsed. Useful for time travel.
def add_time(start, duration, day = ""):
    start_dict = split_time(start)
    duration = split_time(duration)
    mins_start = time_to_mins(start_dict)
    mins_dur = time_to_mins(duration)
    mer = start_dict["meridian"]
    if mer == "PM":
        mins_start = mins_start + 720 #adds the 12 morning hours if time is in afternoon
    total_mins = mins_dur + mins_start
    ret_days = make_days(total_mins)
    ret_hours = make_hours(total_mins)
    ret_min = make_minutes(total_mins)
    ret_mer = make_mer(total_mins)
    if day == "":
        return str(ret_hours) + ':' + str(ret_min) + ' ' + ret_mer + ret_days
    else:
        ret_day_of_the_week = make_day_of_the_week(total_mins, day)
        return str(ret_hours) + ':' + str(ret_min) + ' ' + ret_mer + ret_day_of_the_week + ret_days

#Takes string input and creates dictionary that can be utilized for calculating times
def split_time(time):
    hour = time.split(":").pop(0)
    minute = time.split(" ")[0].split(":").pop()
    meridian = ""
    if time.split(" ")[0] == time:
        return({"hour": hour, "minute": minute})
    else:
        meridian = time.rsplit(" ").pop()
        return({"hour": hour, "minute": minute, "meridian": meridian})

#Converts the split_time dictionaries to minutes to be used in calculation functions
def time_to_mins(dict):
    time = int(dict["hour"]) * 60 + int(dict["minute"])
    return time

#Functions to find the minutes, hours, meridian, days, and day of the week based on the minutes elapsed.
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

#This is kind of neat. Every 12 hours, the meridian switches, so I used floor division to determine if the hour/12 is even or odd. When even, it's morning, when odd, it's evening. So morning = 0, 2, 4 and evening = 1, 3, 5 etc.
def make_mer(min):
    hours = min // 60
    if (hours // 12) % 2 == 0:
        mer = "AM"
    else: mer = "PM"
    return mer

def make_days(min):
    days = ""
    days = min // 1440 #1440 is the number of minutes in a day
    if days > 1:
        days = " (" + str(days) + " days later)"
    elif days == 1:
        days = " (next day)"
    else:
        days = ""
    return(days)

def make_day_of_the_week(min, day):
    day = day.title()
    days = min // 1440 #ibid. Because my make_days function returned strings, I had to redor the math here.
    index = days_of_the_week.index(day)
    index = (index + days) % 7
    day_of_the_week = ", " + days_of_the_week[index]
    return day_of_the_week

print(add_time('3:30 PM', '2:12')) #should return '5:42 PM'.
print(add_time('11:55 AM', '3:12')) #should return '3:07 PM'.
print(add_time('2:59 AM', '24:00')) #should return '2:59 AM (next day)'.
print(add_time('11:59 PM', '24:05')) # should return '12:04 AM (2 days later)'.
print(add_time('8:16 PM', '466:02')) # should return '6:18 AM (20 days later)'.
print(add_time('3:30 PM', '2:12', 'Monday')) #should return '5:42 PM, Monday'.
print(add_time('2:59 AM', '24:00', 'satuRday')) #should return '2:59 AM, Sunday (next day)'.
print(add_time('11:59 PM', '24:05', 'Wednesday')) #should return '12:04 AM, Friday (2 days later)'.
print(add_time('8:16 PM', '466:02', 'tueSday')) #should return '6:18 AM, Monday (20 days later)'.