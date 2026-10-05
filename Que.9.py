#Write a program to swap two numbers without using third variable.
#take input

a = int(input('Enter the value of a :'))
b = int(input('Enter the value of b :'))

#perform operation

a = a + b
b = a - b
a = a - b


#display 
print(f'After swap a is {a}')
print(f'After swap b is {b}')