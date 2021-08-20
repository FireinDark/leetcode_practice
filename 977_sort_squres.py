
def sortedSquares(nums):
    resp = list()
    left = 0
    right = len(nums) - 1
    while left <= right:
        l = nums[left] ** 2
        r = nums[right] ** 2
        if l > r:
            resp.append(l)
            left += 1
        else:
            resp.append(r)
            right -= 1
    return resp[::-1]
        
        



if __name__ == '__main__':
    print(sortedSquares([-4,  -3, -1, 0, 3, 10]))
    