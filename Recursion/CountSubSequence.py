# [1,2,1] sm=2
# op - 2


n = 3
arr = [1, 2, 1]
resArr = []
newArr = []
currSm = 0
sm = 2


def findSeqSum(ind, n, sm, currSm):
    if ind >= n:
        if sm == currSm:
            return 1
        return 0
    else:
        currSm += arr[ind]
        l = findSeqSum(ind+1, n, sm, currSm)
        currSm -= arr[ind]
        r = findSeqSum(ind+1, n, sm, currSm)
        return l+r


print(findSeqSum(0, n, sm, currSm))
