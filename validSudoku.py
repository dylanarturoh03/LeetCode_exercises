class Solution:
    def isValidSudoku(self, board = list[list[str]]) -> bool:
        boxes = {i : set() for i in range(9)}
        rows = {i : set() for i in range(9)}
        colums = {i : set() for i in range(9)}
        digits = {'1','2','3','4','5','6','7','8','9'}
        box = 0

        # We check duplicates in 3 X 3 boxes and rows
        for i, row in enumerate(board):
            for j, element in enumerate(row):


                if (element in boxes[box] and element in digits) or (element in rows[i] and element in digits): 
                    return False
                
                rows[i].add(element)
                boxes[box].add(element)
                if (j+1) %3 == 0:
                    box+=1
                
            if (i+1) %3 != 0:
                box -= 3


        # We check duplicates in columns

        row = 0

        while row < 9:

            for col in range(9):
                if board[col][row] in colums[row] and board[col][row] in digits:
                    return False
                
                colums[row].add(board[col][row])
            
            row+=1
        
        return True 
    
sol = Solution()
print(sol.isValidSudoku(
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
))