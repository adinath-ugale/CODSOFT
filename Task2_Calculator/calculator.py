while True:
    print("\n_ - _ - SIMPLE CALCULATOR - _ - _")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except:
        print("Invalid input! Please enter numbers.")
        continue

    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print("Result:", num1 + num2)

    elif choice == '2':
        print("Result:", num1 - num2)

    elif choice == '3':
        print("Result:", num1 * num2)

    elif choice == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error! Division by zero")
#choice
    else:
        print("Invalid choice")

    again = input("\nDo you want to calculate again? (yes/no): ").lower()
    if again != 'yes':
        print("Calculator closed. Thank you Visit in calculator!")
        break
        
