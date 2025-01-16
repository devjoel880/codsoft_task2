
def calculator():
    print("Basic Calculator App\n")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except:
        print("Invalid input. Enter a numeric value")

    print("\nChoose an Operation: ")
    print(
        "1. Addition (+), "
        "2. Subtraction (-), "
        "3. Multiplication (*), "
        "4. Division (/)\n"
    )
    choice = input("Enter the number of your choice (1, 2, 3, 4): ")

    match choice:
        case "1":
            operation = "+"
            result = num1 + num2
        case "2":
            operation = "-"
            result = num1 - num2
        case "3":
            operation = "*"
            result = num1 * num2
        case "4":
            operation = "/"
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by Zero (0) is not allowed")
                return
        case _:
            print("Invalid choice. Please select a valid option")
            return

    print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()
