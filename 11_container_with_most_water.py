class Solution:
    # 暴力算法
    # def maxArea(self, height) -> int:
    #     length = len(height)
    #     max_value = 0
    #     for i in range(length-1):
    #         for j in range(i+1, length):
    #             v = min([height[i], height[j]]) * (j-i)
    #             max_value = max_value if v <= max_value else v
    #     return max_value
    
    # 双指针，类似滑窗
    def maxArea(self, height) -> int:
        length = len(height)
        max_area = 0
        start = 0
        end = length - 1
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            max_area = max_area if max_area >= area else area
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return max_area

        
        
    

if __name__ == '__main__':
    c = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(c))

    