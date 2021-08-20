

def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast]:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums

if __name__ == '__main__':
    print(moveZeroes([0,1,0,3,12]))
    print(moveZeroes([0,0,0,3,12]))
    