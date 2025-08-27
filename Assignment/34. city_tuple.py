# wap how many cit name is present count

t1 = ('pune', 'banglore', 'delhi', 'pune', 'mumbai')
x = input("Enter a city = ")
if x in t1:
    print(t1.count(x))
else:
    print('city not present')
