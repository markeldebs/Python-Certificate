def add_time(start, duration, day = ''):

    start_split = []

    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

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

    # Converting back to 12-hour time format
    n_days = 0
    while new_day_hours >= 12:

        n_days += 1
        new_day_hours -= 12


    if n_days%2 == 0:
        new_day_phase = "AM"
    else:
        new_day_phase = "PM"


    # Determining n days
    # (n_days/2).__floor__()

    if day != '':
        day = week[(week.count(day))+ (n_days/2).__floor__()]
    

    # Creating return string
    new_time = str(new_day_hours)+":"+ str(new_day_minutes)+ " " +new_day_phase + " " + day
    new_time.rstrip()


    return(new_time)


    # expected = "5:42 PM"

print(add_time("3:30 AM", "22:12", "Monday"))

