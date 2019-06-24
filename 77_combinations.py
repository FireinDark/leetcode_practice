

# 利用C(m, n) = C(m-1, n) + C(m-1, n-1)

class Solution:
    def combine(self, n: int, k: int):
        if k>n or k==0:
            return []
        if k==1:
            return [[i] for i in range(1,n+1)]
        if k==n:
            return [[i for i in range(1,n+1)]]
        # 第一个序列
        answer=self.combine(n-1,k)
        for item in self.combine(n-1,k-1):
            item.append(n)
            answer.append(item)
        return answer
 

if __name__ == '__main__':
    s = Solution().combine(5, 3)
    print(s)
