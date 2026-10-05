#Convert the time entered in hh,min and sec into seconds.
#take input
hours = int(input('Enter the hour:'))
min = int(input('Enter the minute:'))
sec = int(input('Enter the second:'))

#perform operation
total = (hours * 3600) + (min* 60) + sec

# Display result
print(f'Seconds is {total}')
