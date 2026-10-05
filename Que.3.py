#Convert distant given in feet and inches into meter and centimeter.
#take input
feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))

# Convert total distance to inches
total_inches = (feet * 12) + inches

# Convert to centimeters
total_cm = total_inches * 2.54

# Convert to meters and centimeters
meters = int(total_cm // 100)
centimeters = total_cm % 100

#display distant in centimeter and meter
print(f'Distant in meter is {meters} and centimeter is {centimeters}')