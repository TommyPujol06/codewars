sudoku = []
for _ in range(3):
    inp = input().split()
    for n in inp:
        sudoku.append(int(n))

nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}

missing = []
for num in nums:
    if num not in sudoku:
        missing += [num]

if not missing:
    print("This is a valid sudoku")
else:
    print("This is an invalid sudoku. Missing numbers are:")
    for n in missing:
        print(n)
