

def search_range(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            l = mid - 1
            while l >= 0:
                if nums[l] != target:
                    break
                l -= 1
            r = mid + 1
            while r <= len(nums) - 1:
                if nums[r] != target:
                    break
                r += 1
            return [l+1, r-1]
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return [-1, -1]

if __name__ == '__main__':
    print(search_range([5,7,7,8,8,10], 8))
    print(search_range([5,7,7,8,8,10], 6))
    print(search_range([5,7,7,8,8,10], 0))
    
        