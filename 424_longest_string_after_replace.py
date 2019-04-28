# -*- coding: utf-8 -*-
__author__ = 'yi.liu'


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = end = 0
        char_list = [0 for _ in range(26)]
        position_a = ord('A')
        while len(s) > end:
            char_list[ord(s[end]) - position_a] += 1
            # 窗口长度大于 可替换次数与重复最多字母的次数，
            # 此时不能进行替换，说明可以右移，增加窗口长度
            if sum(char_list) > (k + max(char_list)):
                char_list[ord(s[start]) - position_a] -= 1
                start += 1
            end += 1
        # 当我们找到一个最大的窗口之后，
        # 之后的每一次操作都是移动此窗口
        # 所以窗口长度就是我们的最大长度
        return end - start


if __name__ == '__main__':
    print(Solution().characterReplacement("SAFSSJKFJKKWQRSS", 2))
