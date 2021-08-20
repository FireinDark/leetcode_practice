

def isValid(s):
    info = {"(": ")", "[": "]", "{": "}"}
    right = 0
    left = list()
    while right < len(s):
        if s[right] in info:
            left.append(s[right])
        else:
            if s[right] != info.get(left[-1]):
                return False
            left.pop()
        right += 1
    return not left


if __name__ == '__main__':
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
    print(isValid("([)]"))
    print(isValid("{[]}"))
    print(isValid("(([]){})"))
    