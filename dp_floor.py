

def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 1 + dp(2) + dp(1)
    if n == 4:
        return 1 + dp(3)+ dp(2) + dp(1)
    return dp(n-4) + dp(n-3) + dp(n-2)+dp(n-1)

if __name__ == '__main__':
    print(dp(4))
    