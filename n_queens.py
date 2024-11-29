import time

def solve_n_queens(n):
    board = [['.'] * n for _ in range(n)]
    solutions = []
    
    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def backtrack(row):
        if row == n:
            solutions.append(['|'.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
    
    backtrack(0)
    return solutions

# Example usage
n = 4
start = time.time()
solutions = solve_n_queens(n)
print(solutions)
print(f"Number of solutions for {n}-queens: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(row)
    print()
end = time.time()
print(end - start)


def solve_nq(n):
    board = [['.'] * n  for _ in range(n)]
    cols = set()
    pdiag = set()
    ndiag = set()

    res = []

    def backtrack(r):
        if r == n:
            copy = ['|'.join(row) for row in board]
            res.append(copy)
            return 

        for c in range(n):
            if c in cols or (r+c) in pdiag or (r-c) in ndiag:
                continue
            board[r][c]='Q'
            cols.add(c)
            pdiag.add(r+c)
            ndiag.add(r-c)

            backtrack(r+1)

            board[r][c]='.'
            cols.remove(c)
            pdiag.remove(r+c)
            ndiag.remove(r-c)
    backtrack(0)
    return res
start = time.time()
sol = solve_nq(4)
for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print()
end = time.time()
print(end - start)