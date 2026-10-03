class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return self.isValidSudokuUsingHashSet(board)
        # return self.isValidSudokuUsingFreqTable(board)

    def isValidSudokuUsingHashSet(self, board: list[list[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

    def isValidSudokuUsingFreqTable(self, board: list[list[str]]) -> bool:
        rowFreq = [[0 for x in range(9)] for x in range(9)]
        colFreq = [[0 for x in range(9)] for x in range(9)]
        boxFreq = [[0 for x in range(9)] for x in range(9)]

        boxIndex = 0
        for i in range(len(board)):
            boxRowIndex = math.floor(i/3) * 3

            for j in range(len(board[i])):
                if(board[i][j] == "."):
                    continue

                boxColIndex = math.floor(j/3)
                boxIndex = boxRowIndex + boxColIndex

                currNum = int(board[i][j]) - 1

                boxFreq[boxIndex][currNum] += 1
                rowFreq[i][currNum] += 1
                colFreq[j][currNum] += 1

        # Check if any cell in rowFreq, colFreq, or boxFreq is greater than 1
        if (any(val > 1 for row in rowFreq for val in row) or
            any(val > 1 for col in colFreq for val in col) or
            any(val > 1 for box in boxFreq for val in box)):
            return False
        
        return True

