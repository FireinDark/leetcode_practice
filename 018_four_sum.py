
def fourSum(nums, target):
    length = len(nums)
    if length < 4:
        return []
    if length == 4 and sum(nums) == target:
        return [nums]
    result = list()
    nums.sort()

    for i in range(length-3):
        if nums[i] > (target/4):
            continue
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, length-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            c = j + 1
            d = length - 1
            while c < d:
                r = nums[i] + nums[j] + nums[c] + nums[d]
                if r == target:
                    result.append([nums[i], nums[j], nums[c], nums[d]])
                    while c < d and nums[c] == nums[c+1]:
                        c += 1
                    while c < d and nums[d] == nums[d-1]:
                        d -= 1
                    c += 1
                    d -= 1
                elif r > target:
                    d -= 1
                else:
                    c += 1
    return result
