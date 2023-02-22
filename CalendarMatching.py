from datetime import datetime

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Combine the calendars and sort by start time
    calendar = calendar1 + calendar2
    calendar.sort()

    # Add daily bounds to the beginning and end of the calendar
    calendar = [['00:00', dailyBounds1[0]]] + calendar + [[dailyBounds1[1], '23:59']]
    calendar = [['00:00', dailyBounds2[0]]] + calendar + [[dailyBounds2[1], '23:59']]

    # Loop through the calendar and find all the available time blocks
    availableBlocks = []
    for i in range(1, len(calendar)):
        start = calendar[i-1][1]
        end = calendar[i][0]
        if timeDifference(start, end) >= meetingDuration:
            availableBlocks.append([start, end])

    # Convert available time blocks to military time
    for i in range(len(availableBlocks)):
        availableBlocks[i][0] = toMilitaryTime(availableBlocks[i][0])
        availableBlocks[i][1] = toMilitaryTime(availableBlocks[i][1])

    return availableBlocks

# Helper function to calculate the time difference between two time strings
def timeDifference(start, end):
    start = datetime.strptime(start, '%H:%M')
    end = datetime.strptime(end, '%H:%M')
    diff = end - start
    return diff.total_seconds() // 60

# Helper function to convert a time string to military time
def toMilitaryTime(timeString):
    time = datetime.strptime(timeString, '%H:%M')
    return time.strftime('%H:%M')


calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30
output=calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
print(output)
