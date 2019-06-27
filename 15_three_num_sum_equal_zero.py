class Solution:
    def threeSum(self, nums):
        nums.sort()
        r = set()
        if nums[0] > 0:
            return list(r)
        if nums[0] == 0 and nums[-1] == 0:
            return [[0, 0, 0]]
        length = len(nums)
        start = 0
        while start < length-2:
            if nums[start] > 0:
                break
            for i in nums[start+1:length-1]:
                if (-i - nums[start]) in nums[start+2:]:
                    r.add((nums[start], i, -i - nums[start]))
            start += 1
        return list(r)


if __name__ == '__main__':
    print(Solution().threeSum([-2,0,1,1,2]))
    
