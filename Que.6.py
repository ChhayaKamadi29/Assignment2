#WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic
#take input
basic = float(input("Enter basic salary: "))

#calculate  total salary
da = 10 / 100 * basic
ta = 12 / 100 * basic
hra = 15 / 100 * basic
salary = basic + da + ta + hra

#display salary
print(f'The total salary is {salary} ')