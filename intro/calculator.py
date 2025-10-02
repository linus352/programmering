number_1 = input()
number_1 = int(number_1)

number_2 = input()
number_2 = int(number_2)

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

print("Vad vill du göra?")
print("1. Addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

choice = input()

if choice == "1":
    result = addition(number_1, number_2)
    print(result)

if choice == "2":
    result = subtraction(number_1, number_2)
    print(result)
    
if choice == "3":
    result = multiplication(number_1, number_2)
    print(result)

if choice == "4":
    result = division(number_1, number_2)
    print(result)