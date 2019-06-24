class Solution:
    def myAtoi(self, str: str) -> int:
        symbol = ["-", "+"]
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        num = ""
        s = str.strip()
        print(s)
        if not s:
            return 0
        if len(s) == 1 and s[0] not in nums:
            return 0
        if s[0] in symbol or s[0] in nums:
            num += s[0]
            for i in s[1:]:
                if i in nums:
                    num += i
                else:
                    break
        if (not num) or (num == '-') or (num =="+"):
            return 0
        num = int(num)
        if num < -2147483648:
            return -2147483648
        if num > 2147483648:
            return 2147483648
        return num

if __name__ == '__main__':
    s = Solution().myAtoi("               -4193 with words")
    print(s)
    