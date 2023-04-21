class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        transposed = []
        
        for i in range(len(matrix[0])):
            col = []
            for mat in matrix:
                col.append(mat[i])
            transposed.append(col)
        
        return transposed
            
