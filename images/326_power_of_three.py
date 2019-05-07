# -*- coding: utf-8 -*-
__author__ = 'yi.liu'


class Solution(object):
    # 递归
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if int(n) - n != 0:
            return False
        if n <= 0:
            return False
        if n == 1:
            return True
        return self.isPowerOfThree(n/3)

    # 将整数转换成3进制则必为10开头，如 10进制，10的n次方表示为 10， 100， 1000
    # 那么 3的N次方3进制也表示为 10， 100，1000

    # 另外整数范围内3的最大幂为1162261467， 而且3的质因子只有3，所以只需 1162261467 % n == 0就行

if __name__ == '__main__':
    print(Solution().isPowerOfThree(45))