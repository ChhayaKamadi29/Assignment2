#Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

#take input
cel = float(input('Enter the temp in celsius:'))

#calculate fahrenheit
Far = (cel * 9 / 5) + 32

#display temp
print(f'Temperature is {Far}')
