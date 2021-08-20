

from typing import NoReturn


def remove_ele(nums, val):
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        else:
            left += 1
    return left
    

if __name__ == '__main__':
    print(remove_ele([0,1,2,2,3,0,4,2], 2))
    # print(remove_ele([3,2,2,3], 3))
    # print(remove_ele([1], 1))
    # print(remove_ele([4, 5], 5))
       