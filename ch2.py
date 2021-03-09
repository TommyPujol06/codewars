filed = []
while True:
    inp = input()
    if inp == "#":
        break
    
    filed.append(inp)

total_cm = 0
for row in filed:
    for c in row:
        if c == 'o':
            total_cm += 1
        elif c == '+':
            total_cm += 1.5
        elif c == 'T':
            total_cm += 2

print(total_cm)
