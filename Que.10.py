#Write a program to reverse three-digit number.
#take input
num = int(input('Enter the number:'))

# perform operation

a = num // 100
b = (num // 10) % 10
c = num % 10

reverse = c * 100 + b * 10 + a

#display 

print(f'The reverse value is {reverse}')