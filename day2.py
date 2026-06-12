# ============================================
#  DAY 2 - Functions, While Loop, Dictionaries
# ============================================

# 1. WHILE LOOP
count = 1

while count <= 5:
	print(f"Count is {count}")
	count = count + 1 

# 2. FUNCTIONS
def greet(name):
	print(f"Hello, {name}!")

greet("Aditya")
greet("Rahul")
greet("Priya")

# 3. FUNCTION WITH RETURN
def add_numbers(a, b):
	return a + b 

result = add_numbers(10, 5)
print(result)

# 4. DICTIONARIES
student = {
	"name": "Aditya",
	"age": 18,
	"city": "Beed"
}

print(student["name"])
print(student["age"])
print(student["city"])

# 5. TYPE CONVERSION
num_str = "100"
print(type(num_str))

num_int = int(num_str)
print(type(num_int))

print(num_int + 50)

# 6. MINI PROJECT - SIMPLE CALCULATOR
def calculator(num1, num2, operation):
	if operation == "add":
		return num1 + num2
	elif operation == "subtract":
		return num1 - num2
	elif operation == "multiply":
		return num1 * num2
	elif operation == "divide":
		return num1 / num2
	else:
		return "Invalid operation"

print(calculator(10, 5, "add"))
print(calculator(10, 5, "subtract"))
print(calculator(10, 5, "multiply"))
print(calculator(10, 5, "divide"))

# 7. STRING METHODS
name = "  Aditya Mohalkar  "

print(name.upper())
print(name.lower())
print(name.strip())
print(name.replace("Aditya", "Rahul"))
print(len(name))

# 8. LIST METHODS
prices = [100, 250, 80, 320]

prices.append(500)
print(prices)

prices.remove(80)
print(prices)

print(max(prices))
print(min(prices))
print(sum(prices))

# 9. LIST OF DICTIONARIES
portfolio = [
    {"stock": "Apple", "price": 180, "qty": 10 },
    {"stock": "Tesla", "price": 250, "qty": 5},
    {"stock": "Google", "price": 140, "qty": 8}
]

for item in portfolio:
	total = item["price"] * item["qty"]
	print(f"{item['stock']}: {item['qty']} shares at {item['price']} = {total}")

# 10. TOTAL PORTFOLIO VALUE
portfolio = [
    {"stock": "Apple", "price": 180, "qty": 10},
    {"stock": "Tesla", "price": 250, "qty": 5},
    {"stock": "Google", "price": 140, "qty": 8}
]

total_value = 0

for item in portfolio:
	value = item["price"] * item["qty"]
	total_value = total_value + value 

print(f"Total Portfolio Value: {total_value}")
