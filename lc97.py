# bruce force dfs. O(2^(m+n))

def gen(l3,l1,l2):
        if len(l1) == 0 or len(l2)==0: return [l3+l1+l2]
        comb = []
        comb += gen(l3+l1[0], l1[1:], l2) + gen(l3+l2[0], l1, l2[1:])
        return comb

print(gen("", 'ab','cd'))


# dfs with memo O(m*n)
# 加入s1,s2为ab，cd
# 那么BF会算两次(ac,b,d)(ca,b,d)
# 如果序列更长，这个重复次数会n！的速度增加
# 所以把剩下的字符串存起来memo(b,d) = True
# 加速
def isInterleave1(s1: str, s2: str, s3: str):
        def interleave(s1,i,s2,j,s3,k, memo):
            if len(s1) == i: return s2[j:] == s3[k:]
            if len(s2) == j: return s1[i:] == s3[k:]
            if memo[i][j] >= 0:
                return memo[i][j] == 1
            ans = False
            if (s3[k] == s1[i] and interleave(s1, i+1, s2, j, s3, k+1, memo)) or\
            (s3[k] == s2[j] and interleave(s1,i,s2,j+1,s3,k+1,memo)):
                ans = True
            memo[i][j] = 1 if ans else 0
            return ans
        memo = [[-1]* len(s2) for _ in range(len(s1))]
        return interleave(s1,0,s2,0,s3,0,memo)
            