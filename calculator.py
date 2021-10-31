def sum(number1, number2):
    return number1+number2

def subtract(number1, number2):
    return number1-number2

def divide(number1, number2):
    return number1/number2

def multiply(number1, number2):
    return number1*number2

print("Select a mathematical operation from below:")
print("1. Sum\n2. Subtract\n3. Divide\n4. Multiply")

while True:

    choice = input("Enter your choice(1-2-3-4) ")

    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", sum(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        
        elif choice == '3':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '4':
            print(num1, "*", num2, "=", multiply(num1, num2))

        nextCalculation = input("Do you want to do a new calculation? (yes/no)")

        if nextCalculation == "no":
            break

    else:
        print("Invalid input.")