def simple_intrest(principal, rate, time):
    return (principal * rate * time) / 100

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))

interest = simple_intrest(p, r, t)
print("The simple interest is:", interest)

