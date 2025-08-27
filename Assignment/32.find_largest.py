l1 = []
print("Enter element = ")
for i in range(5):
    l1.append(int(input()))

maxi = l1[0]
for i in range(5):
    if l1[i] > maxi:
        maxi = l1[i]

print("largest = ", maxi)
