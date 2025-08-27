daynames = {'monday', 'tuesday', 'wednesday', 'thursdays', 'friday'}

user_in = input("Enter a day = ")

if user_in in daynames:
    print(user_in, "present")
else:
    print("Not present")