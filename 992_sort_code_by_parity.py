class Solution:
    def sortArrayByParityII(self, A):
        evenid = 0
        oddid = 1
        res = [0] * len(A)
        for a in A:
            if a%2 == 0:
                res[evenid] = a
                evenid += 2
            else:
                res[oddid] = a
                oddid += 2
        return res