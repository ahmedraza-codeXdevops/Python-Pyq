try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    result = a / b
    print("Result=", result)

except ValueError:
    print("Invalid input! Please enter a valid integer.")

except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

except Exception as e:
    print("An unexpected error occurred:", str(e))