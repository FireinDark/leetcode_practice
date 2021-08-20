

def get_next(s):
    # 后缀匹配指向
    i = 1
    # 前缀匹配指向
    j = 0
    next_val = [0 for _ in s]
    while i < len(s):
        # 比较不相等并且此时比较的已经是第一个字符了
        if j == 0 and s[i] != s[j]:
            next_val[i] = 0
            i += 1
        # 比较不相等,将j值设置为ｊ前一位的next_val中的值，为了在之前匹配到的子串中找到最长相同前后缀
        elif s[j] != s[i] and j != 0: 
            j = next_val[j-1]
        elif s[j] == s[i]:   # 相等则继续比较
            next_val[i] = j+1
            j = j+1
            i = i+1
    return next_val


print(get_next("abcdabc"))