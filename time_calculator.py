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
    hours = int(start_dict["hour"]) + int(duration["hour"])
    minutes = int(start_dict["minute"]) + int(duration["minute"])
    mer = start_dict["meridian"]
    if minutes > 59:
        hours = hours + (minutes // 60)
        print(hours)
        minutes = minutes % 60
        if minutes < 10:
            minutes = "0" + str(minutes)
        if hours // 12 % 2 != 0:
            print(hours)
            mer = meridian_cycle(mer)
        if hours > 12:
            print(hours)
            hours = hours - 12
    new_time = str(hours) + ":" + str(minutes) + " " + mer
    print(new_time)
    return new_time

def split_time(time):
    hour = time.split(":").pop(0)
    minute = time.split(" ")[0].split(":").pop()
    meridian = ""
    if time.split(" ")[0] == time:
        return({"hour": hour, "minute": minute})
    else:
        meridian = time.rsplit(" ").pop()
        return({"hour": hour, "minute": minute, "meridian": meridian})

def meridian_cycle(mer):
    mer = "AM" if mer == "PM" else "PM"
    return mer

add_time('3:30 PM', '2:12') #should return '5:42 PM'.
add_time('11:55 AM', '3:12') #should return '3:07 PM'.
# add_time('2:59 AM', '24:00') #should return '2:59 AM (next day)'.
add_time('11:59 PM', '24:05') # should return '12:04 AM (2 days later)'.
# add_time('8:16 PM', '466:02') # should return '6:18 AM (20 days later)'.
# add_time('3:30 PM', '2:12', 'Monday') #should return '5:42 PM, Monday'.
# add_time('2:59 AM', '24:00', 'saturDay') #should return '2:59 AM, Sunday (next day)'.
# add_time('11:59 PM', '24:05', 'Wednesday') #should return '12:04 AM, Friday (2 days later)'.
# add_time('8:16 PM', '466:02', 'tuesday') #should return '6:18 AM, Monday (20 days later)'.
#Waiting:3. Expected time to end with '(next day)' when it is the next day.
#Waiting:4. Expected period to change from AM to PM at 12:00.
#Waiting:8. Expected adding 0:00 to return the initial time.