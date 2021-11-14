"""1329. Sort the Matrix Diagonally (MEDIUM)
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and 
going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], 
where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2]. Given an m x n matrix mat of integers, sort 
each matrix diagonal in ascending order and return the resulting matrix."""

class Solution:
    from collections import defaultdict
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        for m in range(len(mat)):
            for n in range(len(mat[0])):
                dic[m - n].append(mat[m][n])
        for k in dic:
            dic[k] = sorted(dic[k])
        for m in range(len(mat)):
            for n in range(len(mat[0])):
                mat[m][n] = dic[m - n].pop(0)
        return mat
