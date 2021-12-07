class BingoNumber:
    def __init__(self, number, mark) -> None:
        self.number = number
        self.mark = mark
    def __str__(self):
        return "{" + str(self.number) + ", " + str(self.mark) + "}"
    def __repr__(self):
        return "{" + str(self.number) + ", " + str(self.mark) + "}"

def checkWin(board: list) -> int:
    linecount = 0
    columncount = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c].mark == 1:
                linecount +=1
        if linecount == 5:
            return 1
        linecount = 0
    for c in range(len(boards[0])):
        for r in range(len(board)):
            if board[r][c].mark == 1:
                columncount += 1
        if columncount == 5:
            return 1
        columncount = 0
    return 0

def calculateScore(winningNumber: int, board: list) -> int:
    sum: int = 0
    for line in board:
        for x in line:
            if x.mark == 0:
                sum += x.number
    return sum * winningNumber

f = open("day04_input.txt", "r")

numbers = f.readline().strip().split(',')
numbers = [int(num) for num in numbers]
f.readline() # Throw away '\n'
#print(numbers)

input = f.readlines()
f.close()

boards = []
board = []

# Parse boards
for line in input:
    if line == '\n':
        boards.append(board.copy())
        board = []
        continue
    line = line.strip().split()
    line = [BingoNumber(int(x), 0) for x in line]
    board.append(line)

# Process bingo game...
s = []
for num in numbers:
    for board in range(len(boards)):
        for line in range(len(boards[board])):
            for bingonum in range(len(boards[board][line])):
                if num == boards[board][line][bingonum].number:
                    boards[board][line][bingonum].mark = 1
                    #print(boards[board][line][bingonum].number)
    #end

    for board in boards:
        if checkWin(board) == 1:
            s.append(calculateScore(num, board))
            boards.remove(board)
    if not boards:
        break
print(s[0], s[-1])
#print(boards)
#print(input)