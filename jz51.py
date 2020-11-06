def multiply(A):
        # write code here
        right = [A[0]]
        left = [A[-1]]
        for i in range(1,len(A)):
            right.append(right[-1] * A[i])
            left.insert(0, A[len(A)-i-1] * left[0])
        B = []
        for i in range(len(A)):
            l = left[i+1] if i+1 <len(A) else 1
            r = right[i-1] if i > 0 else 1
            B.append(l * r)
        return B

a = [1,2,3,4,5]
print(multiply(a))