

def search_insert(nums, target):
    bottom = 0
    top = len(nums) -1
    while bottom <= top:
        mid = (top + bottom) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            bottom = mid + 1
        else:
            top = mid - 1
    return bottom

if __name__ == '__main__':
    print(search_insert([1,3,5,6], 7))
    print(search_insert([1,3,5,6], 2))
    print(search_insert([1,3,5,6], 0))
    print(search_insert([1], 0))
    