# Your Student ID:230543008
# Your Name and Surname:Emin Talha Celik
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error! Division by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation!")
            return

        print(f"The result of {num1} {operation} {num2} is {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

while True:
    calculator()
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again != "yes":
        break
