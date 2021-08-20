class Solution:
    def getNext(self, n):
        total = 0
        while n:
            total += (n % 10) ** 2
            n //= 10
        return total

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.getNext(n)
            
        print(n)
        return n == 1


if __name__ == '__main__':
    print(Solution().isHappy(19))
    