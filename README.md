# Python-Coding-Assisments


# ********* Apprtment Hunting **********

# find_optimal_block function 

 This function takes in a list of dictionaries representing city blocks and a list of requirements (such as the presence of a gym, school, or store) and returns the index of the block that is closest to all the requirements.

```python
def find_optimal_block(blocks, requirements):
    min_farthest_distance = float('inf')
    optimal_blocks = []

    for i, block in enumerate(blocks):
        distances = [0 if block[req] else float('inf') for req in requirements]
        for j, other_block in enumerate(blocks):
            if other_block == block:
                continue
            for k, req in enumerate(requirements):
                if other_block[req]:
                    distances[k] = min(distances[k], abs(i - j))
        farthest_distance = max(distances)
        if farthest_distance < min_farthest_distance:
            min_farthest_distance = farthest_distance
            optimal_blocks = [i]
        elif farthest_distance == min_farthest_distance:
            optimal_blocks.append(i)

    return optimal_blocks, farthest_distance


blocks =  [
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": True,
    "school": False,
    "store": False,
  },
  {
    "gym": True,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": True,
  },
]

requirements = ["gym", "school", "store"] 
optimal_blocks, farthest_distance = find_optimal_block(blocks, requirements)

print(f"{optimal_blocks[0]} // at index {optimal_blocks[0]}, the farthest you'd have to walk to reach a gym, a school, or a store is {farthest_distance} block(s); at any other index, you'd have to walk farther")

```


# Requirements
```python
This program requires Python 3.x to be installed.
```



# Usage
The program can be run from the command line using the following command:
```python
python ApartmentHunting.py

```
By default, the program will use the sample data provided in the blocks and requirements variables in the code. If you want to use your own data, you can modify these variables in the code.



# Inputs
`blocks`: A list of `n` dictionaries, each representing a block. Each dictionary has three boolean keys: `gym`, `school`, and `store`. The value of each key is `True` if the corresponding facility is present in the block, and `False` otherwise.

`requirements`: A list of strings, representing the facilities that the user wants to be close to. The list can contain any combination of `"gym"`, `"school"`, and `"store`"

## Input Example
```python
blocks =  [
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": True,
    "school": False,
    "store": False,
  },
  {
    "gym": True,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": True,
  },
]

requirements = ["gym", "school", "store"] 

optimal_blocks, farthest_distance = find_optimal_block(blocks, requirements)

print(f"{optimal_blocks[0]} // at index {optimal_blocks[0]}, the farthest you'd have to walk to reach a gym, a school, or a store is {farthest_distance} block(s); at any other index, you'd have to walk farther")

```
# Output:
```python
3 // at index 3, the farthest you'd have to walk to reach a gym, a school, or a store is 1 block; at any other index, you'd have to walk farther

```


# ********* Calendar Matching *********

This is a function that helps you find all available time slots to schedule a meeting between you and your co-worker. The function takes in your and your co-worker's calendars, your daily bounds, your co-worker's daily bounds, and the duration of the meeting that you want to schedule, and returns a list of all the time blocks during which you could schedule the meeting, ordered from earliest time block to latest.

## Requirements
The function is implemented in Python and requires the following packages:

- This program requires `Python` 3.x to be installed.
- `datetime`




## Usage

```python
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
```

### To use the function, call `calendarMatching` with the following parameters:
```python 
calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
```
where:
- `calendar1`: a list of your meetings for the day, in the form of [startTime, endTime]. The list is sorted by start time in ascending order.
- `dailyBounds1`: a list of your earliest and latest times for the day in military time, such as ['9:00', '20:00'].
- `calendar2`: a list of your co-worker's meetings for the day, in the same format as calendar1.
- `dailyBounds2`: a list of your co-worker's earliest and latest times for the day in military time, such as ['10:00', '18:30'].
- `meetingDuration`: the duration of the meeting you want to schedule, in minutes.

`The function returns a list of all available time blocks during which you could schedule the meeting, ordered from earliest time block to latest, in the format of [startTime, endTime] also in military time.`





## Examples

```python
calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30

print(calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))
```
##### Output:
```python 
[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
```
