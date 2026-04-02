class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def to(m, index):
            row = len(matrix)
            col = len(matrix[0])
            return (index//col, index%col)
        L = 0
        R = (len(matrix) * len(matrix[0])) - 1
        while L <= R:
            mid = (L+R)//2
            r = to(matrix, mid)[0]
            c = to(matrix, mid)[1]
            if matrix[r][c] > target:
                R = mid - 1
            elif matrix[r][c] < target:
                L = mid + 1
            else:
                return True
        return False
        