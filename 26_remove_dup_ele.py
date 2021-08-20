

def removeDuplicates(nums):
    if not nums:
        return 0
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow-1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow


if __name__ == '__main__':
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(removeDuplicates([1,1,2]))
    
            
