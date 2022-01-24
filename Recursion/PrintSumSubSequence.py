# [1,2,1] sm=2
# [[1,1], [2]]


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
resArr = []
newArr = []
currSm = 0
sm = int(input())


def findSeqSum(ind, n, newArr, sm, currSm):
    if ind >= n:
        if sm == currSm:
            resArr.append(newArr.copy())
        return
    else:
        newArr.append(arr[ind])
        currSm += arr[ind]
        findSeqSum(ind+1, n, newArr, sm, currSm)
        newArr.pop()
        currSm -= arr[ind]
        findSeqSum(ind+1, n, newArr, sm, currSm)


findSeqSum(0, n, newArr, sm, currSm)
print(resArr)
