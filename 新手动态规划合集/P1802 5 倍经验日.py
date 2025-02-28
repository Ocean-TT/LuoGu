def main():
    n, x = map(int, input().split())
    information = []
    for i in range(n):
        information.append(list(map(int, input().split())))
    dp = [[0] * (x + 1) for _ in range(n + 1)]
    for i in range(1, n + 1, +1):
        for j in range(x, -1, -1):
            if j >= information[i - 1][2]:
                dp[i][j] = max(dp[i-1][j] + information[i - 1][0], dp[i-1][j-information[i - 1][2]] + information[i - 1][1])
            else:
                dp[i][j] = dp[i-1][j] + information[i - 1][0]
    print(dp[n][x] * 5)


if __name__ == '__main__':
    main()
