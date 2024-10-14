def add(x, y):
    # todo
    pass

def subtract(x, y):
    # todo
    pass

def multiply(x, y):
    # todo
    pass

def divide(x, y):
    # todo
    pass

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice not in ("1", "2", "3", "4"):
        print("Invalid Input")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == "1":
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == "2":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

    elif choice == "3":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    elif choice == "4":
        if num2 == 0:
            print("Division by zero is not allowed")
        else:
            print(f"{num1} / {num2} = {divide(num1, num2)}")

    next_calculation = input("Continue calculation? (y/n): ")
    if next_calculation == "n":
        break
