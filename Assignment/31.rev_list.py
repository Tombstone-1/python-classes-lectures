l1 = []
print("Enter element = ")
for i in range(5):
    l1.append(int(input()))

i = len(l1) - 1
while i >= 0:
    print(l1[i])
    i -= 1
