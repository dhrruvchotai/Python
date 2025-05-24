n = 50

num = n * (n + 1) // 2 

for i in range(1, n + 1):
    row = []
    for j in range(i):
        row.append(num)
        num -= 1
    if i % 2 == 0: row = reversed(row)
    spaces = '    ' * (n - i)
    print(spaces + ' '.join(f"{x:4}" for x in row))
