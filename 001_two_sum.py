

def twoSum(nums, target: int):
        info = dict()
        for i, num in enumerate(nums):
            info[num] = i

        for i, num in enumerate(nums):
            if info.get(target-num) and info.get(target-num) != i:
                return [i, info.get(target-num)]


if __name__ == '__main__':
    print(twoSum([3, 2, 4], 6))
    