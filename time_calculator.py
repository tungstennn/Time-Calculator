#def add_time(start, duration, day = False):
 #   new_time = ''
#    start
import re

time = "3:58 PM"

hours = int(time.split(':')[0])
minutes = int(time.split(':')[1].rstrip(' AMP'))

duration = "402:35"
hoursx = int(duration.split(':')[0])
minutesx = int(duration.split(':')[1])

new_time = ''
newmin = minutes + minutesx

change_in_hours = hoursx % 12
if newmin > 59:
    change_in_hours = change_in_hours + 1
    newmin = newmin - 60

print(change_in_hours)

newhr = change_in_hours + hours
if newhr > 12:
    newhr = newhr - 12

if re.search('P', time):
    if change_in_hours % 2 == 0:
        print(time, ' + ', duration, ' = ', newhr, ':', newmin, 'PM')

if re.search('A', time):
    if change_in_hours % 2 == 0:
        print(time, ' + ', duration, ' = ', newhr, ':', newmin, 'PM')


#newhr = hours + hoursx

#if newmin >= 60:
 #   newmin = newmin - 60



#print(str(hours) + ' hours and ' + str(minutes) + ' minutes')