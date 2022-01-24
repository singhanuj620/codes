# [3,1,2]
# [[3, 1, 2], [3, 1], [3, 2], [3], [1, 2], [1], [2]]

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
resArr = []


def findSeq(ind, n, newArr):
    if ind >= n:
        resArr.append(newArr.copy())
        return
    newArr.append(arr[ind])
    findSeq(ind+1, n, newArr)
    newArr.pop()
    findSeq(ind+1, n, newArr)


newArr = []
findSeq(0, n, newArr)
resArr.pop()
print(resArr)
