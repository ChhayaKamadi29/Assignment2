#WAP to calculate selling price of book based on cost price and discount.

#take input
cost_price = float(input("Enter cost price of book: "))
discount = float(input("Enter discount percentage: "))

#calculate selling price
discount_amount = (cost_price * discount) / 100
selling_price = cost_price - discount_amount

#display selling price
print(f'Selling price is {selling_price}')