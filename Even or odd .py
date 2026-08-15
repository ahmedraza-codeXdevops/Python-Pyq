def check_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(f"The number {num} is {check_number(num)}.")