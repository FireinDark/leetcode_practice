





def minWindow(s, t):
    from collections import defaultdict
    need = defaultdict(int)
    for char in t:
        need[char] += 1
    # 记录窗口左端位置
    left = 0
    res = (0, float("inf"))
    need_char = len(t)
    for right, char in enumerate(s):
        if need[char] > 0:
            need_char -= 1
        need[char] -= 1
        # t里面所有字符已经满足，窗口左端右移，排除过多元素, 进行优化
        if need_char == 0:
            while True:
                char = s[left]
                # 等于0 表示此元素为必须元素 刚好满足， 小于0时表示有多余
                if need.get(char) == 0:
                    break
                need[char] += 1
                left += 1
            # 优化成功
            if right - left < res[1] - res[0]:
                res = (left, right)
            # 窗口继续右滑
            need[s[left]] += 1
            need_char += 1
            left += 1
    return '' if res[1] > len(s) else s[res[0]:res[1]+1]
                
            
        


if __name__ == '__main__':
    print(minWindow("ADOBECODEBANC", "ABC"))
    