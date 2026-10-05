#Write a program to swap two numbers using third variable.
#take input

a = int(input('Enter the value for a :'))
b = int(input('Enter the value for b :'))

#perform operation

var = a
a = b
b= var

#display
print(f'After swap a is {a}')
print(f'After swap b is {b}')