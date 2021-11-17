"""1329. Sort the Matrix Diagonally (MEDIUM)
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and 
going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], 
where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2]. Given an m x n matrix mat of integers, sort 
each matrix diagonal in ascending order and return the resulting matrix."""

class Solution:
    from collections import defaultdict
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonal = defaultdict(list)
        # Since the difference between the rows (m) and columns (n) remains constant within the same diagonal, we use this as a
        #  key to keep track of diagonals and the values stored within them.
        for m in range(len(mat)):
            for n in range(len(mat[0])):
                diagonal[m - n].append(mat[m][n])
        # The values within the diagonal are sorted in ascending order
        for k in diagonal:
            diagonal[k] = sorted(diagonal[k])
        # The sorted values are put back into the original array
        for m in range(len(mat)):
            for n in range(len(mat[0])):
                mat[m][n] = diagonal[m - n].pop(0)
        return mat
