# -*- coding: utf-8 -*-
__author__ = 'yi.liu'

class Solution:

    def longestSubstring(self, s: str, k: int) -> int:
        char_times = dict()
        length = len(s)
        max_length = 0
        if length < k:
            return 0
        for i in s:
            if char_times.get(i):
                char_times[i] += 1
            else:
                char_times[i] = 1
        record_list = list()
        j = 0
        for i, v in enumerate(s):
            if char_times[v] < k:
                record_list.append(s[j:i])
                j = i + 1
        if len(record_list) == 0:
            return len(s)
        # 位置关键
        record_list.append(s[j:length])
        for item in record_list:
            max_length = max(max_length, self.longestSubstring(item, k))
        return max_length

    def find_less_char(self, char_times: dict, k: int) -> str:
        less_char = []
        for key, value in char_times.items():
            if value < k:
                less_char.append(key)
        return "".join(less_char)
    # 没看清楚要求返回的最长字符串中每一个元素的出现次数都不得少于k
    # "ababacb" 按以下方法返回5即 ababa 但是在此字符串中b并未出现3次，故不满足
    # def longestSubstring(self, s: str, k: int) -> int:
    #     char_times = dict()
    #     length = len(s)
    #     if length < k:
    #         return 0
    #     for i in s:
    #         if char_times.get(i):
    #             char_times[i] += 1
    #         else:
    #             char_times[i] = 1
    #     less_char = self.find_less_char(char_times, k)
    #     start_index = end_index = max_length = 0
    #     while end_index < length:
    #         if s[end_index] in less_char:
    #             start_index = end_index + 1
    #             end_index = start_index
    #         else:
    #             end_index += 1
    #         if end_index - start_index > max_length:
    #             max_length = end_index - start_index
    #     return max_length
    #
    # def find_less_char(self, char_times: dict, k: int) -> str:
    #     less_char = []
    #     for key, value in char_times.items():
    #         if value < k:
    #             less_char.append(key)
    #     return "".join(less_char)


if __name__ == '__main__':
    print(Solution().longestSubstring("bbaaacbd", 3))