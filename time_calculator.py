def add_time(start_time, duration, days_needed=" "):

    time= start_time.split()
    time2=time[0].split(":")
    am_pm = time[1]
    split_duration=duration.split(":")

    """Check if time is AM or PM"""
    if am_pm == "PM":
        time2[0]=int(time2[0])+12

    """Add duration to start time"""

    time2[0]=int(time2[0])+int(split_duration[0])
    time2[1]=int(time2[1])+int(split_duration[1])

    """Check if minutes are greater than 60"""

    if time2[1]>60:
        time2[0]=time2[0]+1
        time2[1]=time2[1]-60

    """Convert to 12hr format"""
    
    days=0
    if time2[0]>24:
        days=time2[0]//24
        time2[0]=time2[0]%24
    
    if time2[0]>0 and time2[0]<12:
        am_pm ="AM"
    
    elif time2[0]==12:
        am_pm="PM"
    elif time2[0] > 12 :
        am_pm = "PM"
        time2[0] -= 12
    else :
        am_pm = "AM"
        time2[0] += 12

    """Count additional days"""

    if days > 0 :
        if days == 1 :
            days_later = " (next day)"
        else :
            days_later = " (" + str(days) + " days later)"
    else :
        days_later = ""

    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    if days_needed != " ":
        weeks = days // 7
        i = week_days.index(days_needed.lower().capitalize()) + (days - 7 * weeks)
        if i > 6 :
            i -= 7
        day = ", " + week_days[i]
    else :
        day = ""
    
    new_time= str(time2[0]) + ":" + \
        (str(time2[1]) if time2[1] > 9 else ("0" + str(time2[1]))) + \
        " " + am_pm + day + days_later

    return new_time
