##https://www.nowcoder.com/practice/c61c6999eecb4b8f88a98f66b273a3cc?tpId=13&tqId=11218&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking&from=cyc_github

## dfs 需要回溯，tip是在递归的前后注意进入的变量变化和出来的变量变化，是否有因为出递归而需要还原的变量
def hasPath( matrix, rows, cols, word):
    # write code here
    if rows == 0 or cols == 0: return False
    visit = {(i,j):False for i in range(rows) for j in range(cols)}
    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,word,matrix, visit, ''):
                return True
    return False
def dfs( i, j, word, matrix, visit, path):
    if word == path: return True
    if i<0 or i>= len(matrix) or j <0 or j>=len(matrix[0]) \
    or visit[(i,j)] == True:
        return False
    visit[(i,j)] = True
    res = dfs(i-1,j,word,matrix, visit, path + matrix[i][j]) or\
    dfs(i+1,j,word[1:],matrix, visit, path + matrix[i][j]) or \
    dfs(i,j-1,word[1:],matrix, visit, path + matrix[i][j]) or\
    dfs(i,j+1,word[1:],matrix, visit, path + matrix[i][j])
    visit[(i,j)] = False
    return res

## test
v = {}
print(v.get('4'))
mm = [['a','a','a'],['b','c','d'],['f','e','e']]
print(mm)
path = 'abcdeef'
print(hasPath(mm,3,3,path), path)