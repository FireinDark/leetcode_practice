class Solution:
    # 暴力解决
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        i = 0
        start = ""
        min_index = None
        for item in strs:
            if min_index is None:
                min_index = len(item)
            else:
                min_index = min_index if len(item) > min_index else len(item)
            
        if not min_index:
            return ""
        status = True
        while status and i < min_index:
            start = strs[0][i]
            for item in strs:
                if item[i] != start:
                    status = False
                    break
            if status:
                i += 1
        return strs[0][:i] or ""
    
    # 仅需比较字符串中最短的与最长字符串最长公共前缀就是结果
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        mi = min(strs)
        ma = max(strs)
        if not mi:
            return ""
        for i in range(len(mi)):
            if ma[i] != mi[i]:
                return mi[:i] or ""
        return mi


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
    

