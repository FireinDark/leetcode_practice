

def reverseStr(s: str, k: int) -> str:
    length = len(s)
    temp = ""
    for i in range(0, length, 2*k):
        if i + 2*k <= length:
            temp = temp + s[i:i+k][::-1] + s[i+k:i+2*k]
        else:
            # 剩余长度大于k 小于2k 反转第一个k
            # if i + k <=length:
            temp = temp + s[i:i+k][::-1] + s[(i+k):]
    return temp


if __name__ == '__main__':
    print(reverseStr("abcdefg", 2))
    