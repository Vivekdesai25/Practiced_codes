# Simple Calculator with a Friendly Interface

def add(j, i):
    return j + i

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, r):
    if y == 0:
        return "Error:Cannot divide by zero."
    return x / r

print("Welcome to the Simple Calculator!")
print("What would you like to do today?")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("\nPlease enter your choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Oops! That doesn't look like a valid number. Please try again.")
            continue

        if choice == '1':
            print(f" whooo You got The result of {num1} + {num2} is {add(num1, num2)}")

        elif choice == '2':
            print(f"The result of {num1} - {num2} is {subtract(num1, num2)}")

        elif choice == '3':
            print(f"The result of {num1} × {num2} is {multiply(num1, num2)}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} ÷ {num2} is {result}")

        next_calculation = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if next_calculation != 'yes':
            print("Thanks for using the calculator. Have a great day!")
            break
    else:
        print("Hmm, that doesn't seem like a valid choice. Please enter 1, 2, 3, or 4.")
