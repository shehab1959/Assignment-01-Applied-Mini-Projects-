#Input from user
item = input("1.Enter Item name: ")
price = input("2.Enter Item price: ")
quantity= input("3.Enter Item quantity: ")

#Convert string to float for calculation(Price, Quantity)
a = float(price)      
print(a)
print(type(a))
b = float(quantity)      
print(b)
print(type(b))

#Calculation of total
Total = a * b
print(f"Total bill: {Total} Taka")



## Alternative way
# A. Inputs
# 1. Ask the user for the item name (string)
item_name = input("Enter the item name: ")

# 2. Ask for the price and convert to a number (float handles decimals)
price = float(input("Enter the price of the item: "))

# 3. Ask for the quantity and convert to an integer
quantity = int(input("Enter the quantity: "))

# B. Calculation
# Compute Total = price * quantity
total_bill = price * quantity

# C. Output
# Print the final bill matching the required format exactly
print(f"Total Bill for {item_name} = {total_bill}")


