

def minSubArrayLen(target, nums):
    length = list()
    for i in range(len(nums)):
        remain = target - nums[i]
        if remain <= 0:
            length.append(1)
            continue
        for j in range(i+1, len(nums)):
            remain = remain - nums[j]
            if remain <= 0:
                length.append(j-i+1)
                break
    if not length:
        return 0
    return min(length)


        


if __name__ == '__main__':
    # print(minSubArrayLen(1, [1,1,1,1,1,1,1,1]))
    # print(minSubArrayLen(7, [2,3,1,2,4,3]))
    print(minSubArrayLen(11, [1, 2, 3, 4, 5]))
