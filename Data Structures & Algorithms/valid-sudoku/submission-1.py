class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        gridMap = defaultdict(set)

        for i, row in enumerate(board):
            for j, num in enumerate(board[i]):
                if num != ".":
                    if num in rowMap[i] or num in colMap[j] or num in gridMap[(i//3, j//3)]:
                        return False
                    rowMap[i].add(num)
                    colMap[j].add(num)
                    gridMap[(i//3,j//3)].add(num)
        return True