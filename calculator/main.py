# A simple calculator

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiply two numbers
def multiply(x, y):
    return x * y


# This function multiply two numbers
def divide(x, y):
    return x / y


# Menu of the calculator
print("Chose Operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Takes input and calculates
while True:

    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '2':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '2':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calc
        # break the while loop if answer is no
        # implement an Exit
        next_calculation = input("Lets do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
