#Find the sum of three-digit number.


#take input
num = int(input('Enter the number:'))

# perform operation
d1 = num % 10
num = num //10

d2 = num %10
num = num //10

d3 = num % 10
num = num // 10

sum = d1 + d2 + d3

#display 
#print(f'Separate digit is{d1}')
#print(f'Separate digit is{num}')

#print(f'Separate digit is{d2}')
#print(f'Separate digit is{num}')

#print(f'Separate digit is{d3}')
#print(f'Separate digit is{num}')

print(f'Sum of three digit is {sum}')