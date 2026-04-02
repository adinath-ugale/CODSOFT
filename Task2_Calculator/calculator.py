print("_ _ _ SIMPLE CALCULATOR _ _ _ ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation to calculate:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Division (/)")
print("4. Multiplication (*)")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print("Result:", num1 + num2)

elif choice == '2':
    print("Result:", num1 - num2)

elif choice == '3':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Division by zero")

elif choice == '4':
    print("Result:", num1 * num2)

else:
    print("Invalid Choice")
