# [1,2,1] sm=2
# [[1,1]]


n = 3
arr = [1, 2, 1]
resArr = []
newArr = []
currSm = 0
sm = 2


def findSeqSum(ind, n, newArr, sm, currSm):
    if ind >= n:
        if sm == currSm:
            resArr.append(newArr.copy())
            return True
        return False
    else:
        newArr.append(arr[ind])
        currSm += arr[ind]
        if(findSeqSum(ind+1, n, newArr, sm, currSm)):
            return True
        newArr.pop()
        currSm -= arr[ind]
        if(findSeqSum(ind+1, n, newArr, sm, currSm)):
            return True
        return False


findSeqSum(0, n, newArr, sm, currSm)
print(resArr)
