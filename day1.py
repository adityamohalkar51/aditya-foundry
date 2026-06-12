# ====================================
#  DAY 1 - Python Basics
# ====================================


# 1. PRINT
print("Hello, Foundry!")
print("My name is Aditya.")
print("Day 1 begins now.")

print("___")

# 2. VARIABLES + F-STRINGS
name = "Aditya"
age = 18
city = "Beed"
print(f"My name is {name}, I am {age}, I live in {city}")

print("___")

# 3. DATA TYPES 
height = 5.9
is_student = True
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

print("___")

# 4. MATH OPERATIONS
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

print("___")

# 5. USER INPUT ( commented out so file runs without stopping)
# user_name = input("Enter your name: ")
# print(f"Hello {user_name}")

# 6. COMMENTS
# Yeh line Python run nahi karega - sirf explanation hai 

print("___")

# 7. IF / ELIF / ELSE
marks = 75
if marks >= 90:
	print("Grade: A")
elif marks >= 75:
	print("Grade: B")
else:
	print("Grade: Fail")

print("___")

# 8. FOR LOOP
for i in range(1, 6):
	print(f"{i} x 5 = {i * 5}")

print("___")

# 9. LISTS
stocks = ["Apple", "Google", "Tesla", "Microsoft"]
print(stocks[0])
print(stocks[2])
print(len(stocks))

for stock in stocks:
	print(f"Stock: {stock}")

