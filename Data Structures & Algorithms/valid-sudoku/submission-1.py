class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Keep track of rows, columns and squares
        # Check if current number is in any of them, then return false
        # Will need to iterated through the entire board

        # We can keep them in hash sets
        # The only tricky part is how to add them when we see them
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                
                if (value in rows[i] 
                    or value in cols[j]
                    or value in squares[(i // 3), (j // 3)]):
                    return False
                
                rows[i].add(value)
                cols[j].add(value)
                squares[(i // 3, j // 3)].add(value)
        
        return True
                
