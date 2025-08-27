num1 = int(input("Enter num1 = "))
num2 = int(input("Enter num2 = "))

print("1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division")

ch = int(input("Enter choice = "))

if ch == 1:
    print("Addition = ", num1+num2)
elif ch == 2:
    print("Subtraction = ", num1 - num2)
elif ch == 3:
    print("Multiplication = ", num1 * num2)
elif ch == 4:
    print("Division = ", num1 // num2)
else:
    print("Wrong input")