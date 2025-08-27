gender = input("Enter gender = ")
age = int(input("Enter age = "))
height = int(input("Enter height = "))

if gender == 'm' and age > 30 and height > 160:
    print("Recruited")
elif gender == 'f' and age > 25 and height > 155:
    print("Recruited")
else:
    print("Not recruited")