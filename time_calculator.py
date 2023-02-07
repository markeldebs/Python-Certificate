def add_time(start, duration, day = ''):

    start_split = []

    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week_lower = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    new_time = start + ' ' + duration + ' ' + day
    new_time.rstrip()
    
    start_split.append(start.split(":"))
    start_split.append(start_split[0][1].split())
    start_split.append(duration.split(":"))

    # Assigning different parts to variabls

    start_minutes = int(start_split[1][0])
    day_phase = start_split[1][1]
    duration_hours = int(start_split[2][0])
    duration_minutes = int(start_split[2][1])
    
    if day_phase ==  "AM":
        start_hours = int(start_split[0][0])
    else:
        start_hours = int(start_split[0][0]) + 12
    
    # Converting to minutes to add for calculation
    total_day_minutes = start_hours*60 + start_minutes
    total_duration_minutes = duration_hours*60 + duration_minutes
    
    new_day_hours = ((total_day_minutes+ total_duration_minutes)/60).__floor__()
    new_day_minutes = (total_day_minutes + total_duration_minutes)%60
    if new_day_minutes < 10:
        new_day_minutes = str("0") + str(new_day_minutes)

    # Converting back to 12-hour time format
    n_days = 0
    while new_day_hours >= 12:
        n_days += 1
        new_day_hours -= 12
    
    if new_day_hours == 0:
        new_day_hours = 12
        
    # print(n_days)
    if n_days%2 == 0:
        new_day_phase = "AM"
    else:
        new_day_phase = "PM"
    
    
    # Determining n days
    # (n_days/2).__floor__()
    # days_later = ""
    # day_counter = (n_days/2).floor()

    days_later = (n_days/2).__floor__()
    
    if day != "":
        week_index = week_lower.index(day.lower())
        # print(week_index)
        week_index = int(n_days/2 + week_index)%7
        day = week[week_index]
        
        
        # Creating print statement
        if days_later == 0:
            new_time = str(new_day_hours)+":"+ str(new_day_minutes)+ " " +new_day_phase +", "+ week[week_index]
        elif days_later == 1:
            new_time = str(new_day_hours)+":"+ str(new_day_minutes)+ " " +new_day_phase +", "+ week[week_index]+ " (next day)"
        else:
            new_time = str(new_day_hours)+":"+ str(new_day_minutes)+ " " +new_day_phase + ", "+ week[week_index] + " (" + str(days_later) + " days later)"
            
        new_time.rstrip()
        return(new_time)
    
    
    
    
    
    
    # if day != "":
    #     days_later == number_day_print + "days later"
    #     if n_days == 2 and day == 'Sunday':
    #         days_later = "next day"
    #         day = "Monday"
    #     elif n_days == 2:
    #         days_later = "next day"
    #         day = week[week.index(day)+1]
    #     while (week.index(day)+ int(n_days/2)) > 6:
    #         if week.index(day) == 6:
    #             day = "Monday"
    #             n_days -= 1
    #         else:
    #             day = week[int(week.index(day))+int((number_day_print))]
        
        
    


    

    # Creating return string
    if days_later == 0:
        new_time = str(new_day_hours)+":"+ str(new_day_minutes)+ " " +new_day_phase
    elif days_later == 1:
        new_time = str(new_day_hours)+":"+ str(new_day_minutes)+ " " +new_day_phase + " (next day)"
    else:
        new_time = str(new_day_hours)+":"+ str(new_day_minutes)+ " " +new_day_phase + " (" + str(days_later) + " days later)"
        
    new_time.rstrip()
    return(new_time)


    # expected = "5:42 PM"

print(add_time("10:55 AM", "24:06", "")) 

