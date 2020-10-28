def printMatrix(matrix):
        # write code here
        if not matrix or matrix == [[]]:
            return 
        m,n = len(matrix), len(matrix[0])
        i,j = 0,0
        direction = 'r'
        count = 0
        res = []
        while count < m*n:
            res.append(matrix[i][j])
            count += 1
            matrix[i][j] = '*'
            if direction == 'r':
                if j+1<n and matrix[i][j+1] != '*':
                    j+= 1
                else:
                    direction = 'd'
                    i+=1
            elif direction == 'd':
                if i+1<m and matrix[i+1][j] != '*':
                    i+= 1
                else:
                    direction = 'l'
                    j -= 1
            elif direction == 'l':
                if j>0 and matrix[i][j-1] != '*':
                    j-= 1
                else:
                    direction = 'u'
                    i-=1
            elif direction == 'u':
                if i>0 and matrix[i-1][j] != '*':
                    i-= 1
                else:
                    direction = 'r'
                    j+=1
        return res

a = [[1,3,2],[2,3,6], [2,7,8]]

print(printMatrix(a))