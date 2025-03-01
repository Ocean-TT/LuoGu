def main():
    n = int(input())
    sift = [0 for _ in range(n+1)]
    for i in range(2, n):
        if sift[i] == 0:
            for j in range(i**2, n+1, i):
                sift[j] = 1
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(2, n+1):
        if sift[i] == 0:
            for j in range(i, n+1):
                dp[j] += dp[j-i]
    print(dp[n])


if __name__ == '__main__':
    main()
