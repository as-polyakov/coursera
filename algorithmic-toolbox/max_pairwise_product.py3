n = int(input())
max1 = max2 = -1
for a in map(int, input().split()):
    if a >= max1:
        max2 = max1
        max1 = a
    elif a >= max2:
        max2 = a

print(max1 * max2)
