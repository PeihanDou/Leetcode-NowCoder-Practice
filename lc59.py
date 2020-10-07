'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
'''
# 双指针，步进
def generateMatrix(n):
        mm = [[0] * n for _ in range(n)]
        i,j = 0,0
        filled = 0
        d = 'r'
        while filled < n**2:
            filled += 1
            mm[i][j] = filled
            if d == 'r':
                if j+1 < n and mm[i][j+1] == 0:
                    j += 1
                else:
                    d = 'd'
                    i += 1
            elif d == 'd':
                if i+1 < n and mm[i+1][j] == 0:
                    i += 1
                else:
                    d = 'l'
                    j -= 1
            elif d == 'l':
                if j > 0 and mm[i][j-1] == 0:
                    j -= 1
                else:
                    d = 'u'
                    i -= 1
            elif d == 'u':
                if i > 0 and mm[i-1][j] == 0:
                    i -= 1
                else:
                    d = 'r'
                    j += 1
        return mm
                    
# 分层处理
def generateMatrix1(n):
        mm = [[0] * n for _ in range(n)]
        max_layers = (n+1)//2
        cnt = 0
        for l in range(max_layers):
            for i in range(l,n-l):
                cnt += 1
                mm[l][i] = cnt
            for i in range(l+1,n-l):
                cnt += 1
                mm[i][n-1-l] = cnt
            for i in range(n-l-2, l-1, -1):
                cnt += 1
                mm[n-l-1][i] = cnt
            for i in range(n-l-2, l, -1):
                cnt += 1
                mm[i][l] = cnt
        return mm