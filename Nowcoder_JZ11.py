##https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8?tpId=13&tqId=11164&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking&from=cyc_github


## 利用技巧  n &= (n-1) 的效果是让二进制的n中最低位的1变成0
## 例如 n = 0x00110100, n-1 = 0x00110011, n&(n-1) = 0x00110000
def NumberOf1(n):
    # write code here
    cnt = 0
    while n!=0:
        cnt += 1
        n &=(n-1)
    return cnt