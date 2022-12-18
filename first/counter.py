file1 = open('inventory.txt', 'r')
lines = file1.readlines()

totals = []

current = 0
for line in lines:
    if line != "\n":
        current += int(line)
    else:
        totals.append(current)
        current = 0

totals.sort(reverse=True)

n = 3
toptotal = 0
print("Top", n, ":")
for i in range(n):
    print(totals[i])
    toptotal += totals[i]

print("Sum of top", n, ":", toptotal)
