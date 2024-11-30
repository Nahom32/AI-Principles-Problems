from typing import Set,List
def solve_n_queens(n):
    '''
        This algorithm finds the output for the n-queens problem with n*n dimension finding the column index.
        This algorithm works using the backtracking approach.
    '''
    answers = []
    def backtrack(row, cols:Set, diag:Set, antidiag: Set,curr:List):
        if row == n:
            answers.append(curr[:])
        
        for col in range(n):
            if not (col in cols or (row - col) in diag or (row + col) in antidiag):
                cols.add(col)
                diag.add(row - col)
                antidiag.add(row + col)
                curr.append(col)

                backtrack(row+1, cols, diag,antidiag,curr)

                cols.remove(col)
                diag.remove(row-col)
                antidiag.remove(row+col)
                curr.pop()
    row = 0
    cols = set()
    diag = set()
    antidiag = set()
    curr = []
    backtrack(row,cols,diag,antidiag,curr)
    return answers
print(solve_n_queens(4))


