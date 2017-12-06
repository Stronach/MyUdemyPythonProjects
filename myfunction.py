#myfunction.py
def minutes_to_hours(minutes, seconds=300):
    hours = minutes / 60 + seconds / 3600
    return hours


print(minutes_to_hours(70, 3600))
