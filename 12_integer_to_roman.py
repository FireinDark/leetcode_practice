class Solution:
    def intToRoman(self, num: int):
        # I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
        # X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
        # C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900
        # 字符          数值
        # I             1
        # V             5
        # X             10
        # L             50
        # C             100
        # D             500
        # M             1000
        ans = ''
    
        ans += 'M' * int(num//1000)
        num = num%1000
        
        ans += 'CM' * int(num//900)
        num = num%900
        
        ans += 'D' * int(num//500)
        num = num%500
        
        ans += 'CD' * int(num//400)
        num = num%400
        
        ans += 'C' * int(num//100)
        num = num%100
        
        ans += 'XC' * int(num//90)
        num = num%90
        
        ans += 'L' * int(num//50)
        num = num%50
        
        ans += 'XL' * int(num//40)
        num = num%40
        
        ans += 'X' * int(num//10)
        num = num%10
        
        ans += 'IX' * int(num//9)
        num = num%9
        
        ans += 'V' * int(num//5)
        num = num%5
        
        ans += 'IV' * int(num//4)
        num = num%4
        
        ans += 'I' * num
        return ans
            

