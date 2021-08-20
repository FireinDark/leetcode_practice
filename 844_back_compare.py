

def backspaceCompare(s, t):
    s_real = ""
    for i in s:
        if i == "#":
            s_real = s_real[:-1]
        else:
            s_real += i
    t_real = ""
    for j in t:
        if j == "#":
            t_real = t_real[:-1]
        else:
            t_real += j
    print(s_real, t_real)
    return s_real == t_real



if __name__ == '__main__':
    print(backspaceCompare("a##c", "#a#c"))
    print(backspaceCompare("a#c", "b"))
    print(backspaceCompare("xywrrmp", "xywrrmu#p"))
    