# https://leetcode.com/problems/combination-sum-ii/

def findSubSeq(ind, l, target, currTarget, newArr, resArr, candidates):
    if ind >= l or currTarget >= target:
        if currTarget == target:
            resArr.append(newArr.copy())
        return
    for i in range(ind, l):
        # print(i,newArr,candidates)
        if i > ind and candidates[i] == candidates[i-1]:
            continue
        if candidates[i] > target:
            break
        newArr.append(candidates[i])
        currTarget += candidates[i]
        findSubSeq(i+1, l, target, currTarget,
                   newArr, resArr, candidates)
        newArr.pop()
        currTarget -= candidates[i]


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
# op = [
# [1, 1, 6],
# [1, 2, 5],
# [1, 7],
# [2, 6]
# ]
candidates.sort()
newArr = []
resArr = []
currTarget = 0
findSubSeq(0, len(candidates), target, currTarget, newArr, resArr, candidates)
print(resArr)
