import sys

def merge_sort(l):
    if len(l) < 2:
        return l
    mid = len(l)//2
    left = l[:mid]
    right = l[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(l1, l2):
    res = []
    while l1 and l2:
        if l1[0] < l2[0]:
            res.append(l1.pop(0))
        else:
            res.append(l2.pop(0))
    
    if l1:
        res += l1
    elif l2:
        res += l2
    return res

while True:
    try:
        
        num = int(input())
        n = list(map(int, input().strip().split(' ')))
        reverse = int(input())
        if reverse==0:    
            print(" ".join(map(str,merge_sort(n))))
        else:
            print(" ".join(map(str,merge_sort(n)[::-1])))
    except:break
