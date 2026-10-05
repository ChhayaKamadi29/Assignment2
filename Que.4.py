#WAP to calculate area of triangle and rectangle
#take input for traingle
base = int(input('Enter the base:'))
height = int(input('Enter the height :'))

#take input for rectangle
len = int(input('Enter the length:'))
breadth = int(input('Enter the breadth:'))


#perform operation
Triangle = 1/2 * base * height

#perform operation for rectangle
Rectangle = len * breadth


#display area and rectangle
print(f'Area of triangle is {Triangle}')
print(f'Area of Rectangle is {Rectangle}')
