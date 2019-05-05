# -*- coding: utf-8 -*-
__author__ = 'yi.liu'

class Solution:
    def maxRotateFunction(self, A) -> int:
        length = len(A)
        total_sum = sum(A)
        last_result = max_result = self.array_sum(A)
        for i in range(1, length):
            # 关键是发现 F(k) = F(k-1) + sum - n * A[n-k]
            result = last_result + total_sum - length * A[length-i]
            if result > max_result:
                max_result = result
            last_result = result
        return max_result

    def array_sum(self, array):
        result = 0
        for i in range(1, len(array)):
            result += i * array[i]
        return result

if __name__ == '__main__':
    print(Solution().maxRotateFunction([4,3,2,6]))