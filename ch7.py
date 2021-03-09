x, y = list(map(int, input().split()))
time = int(input())

board = [[0 for _ in range(y)] for _ in range(x)]

while True:
    inp = input()
    if inp == '#':
        break
    
    px, py = list(map(int, inp.split()))
    board[px][py] = 1

while True:
    if time -10 >= 0:
        time -= 10
    else:
        break
    
    for i, row in enumerate(board):
        new = row[1:-1]
        board[i] = new

    board = board[1:-1]

alive = 0
for row in board:
    for col in row:
        if col == 1:
            alive += 1

print(alive)