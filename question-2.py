from typing import List, Tuple
def isValid(board: List[List[int]], row: int, col: int, target: int) -> bool:
    '''
        This function checks if the board provided is valid
        It checks if the number is repeated in the sudoku board.
    '''
    if target in board[row]:
        return False
    for i in range(len(board)):
        if board[i][col] == target:
            return False
    return True

    
def findEmpty(board: List[List[int]]) -> Tuple[int,int]:
    '''
        This function checks for the empty value and returns its position in the matrix
        if it doesn't find it. It returns (-1,-1)

    '''
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i,j)
    return (-1,-1)
def solveBoard(board: List[List[int]]) -> bool:
    '''
        This piece of code is a recursive implementation for backtracking and finding the best solution for
        the problem.
    '''
    empty_pos = findEmpty(board)
    if empty_pos ==(-1,1):
        return True
    row,column = empty_pos #destructuring assignment of the empty position to the boolean value
    for i in range(1, len(board) + 1):
        if isValid(board, row, column, i):
            board[row][column] = i
        
        if solveBoard(board):
            return True
        board[row][column] = 0
    return False


