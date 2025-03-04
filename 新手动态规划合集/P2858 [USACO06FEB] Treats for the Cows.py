def main():
    N = int(input())
    a = [0 for _ in range(N)]
    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        a[i] = int(input())
    for i in range(N):
        dp[i][i] = a[i] * N
    for i in range(N - 2, -1, -1):
        for j in range(i + 1, N):
            dp[i][j] = max(dp[i + 1][j] + a[i] * (N - j + i), dp[i][j - 1] + a[j] * (N - j + i))
    print(dp[0][N - 1])


if __name__ == '__main__':
    main()
# 递归---记忆化搜索---动态规划
