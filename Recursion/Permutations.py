
def findP(nums, n, ind, resArr):
    if ind >= n:
        resArr.append(nums.copy())
        return
    for i in range(ind, n):
        nums[ind], nums[i] = nums[i], nums[ind]
        findP(nums, n, ind+1, resArr)
        nums[ind], nums[i] = nums[i], nums[ind]


nums = [1, 2, 3]
#  Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
resArr = []
n = len(nums)
findP(nums, n, 0, resArr)
print(resArr)
