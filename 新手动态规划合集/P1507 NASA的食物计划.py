def main():
    h, t = map(int,input().split())
    n = int(input())
    information = []
    dp = [[0]*(t+1) for _ in range(h+1)]
    for i in range(n):
        information.append(list(map(int,input().split())))
    for i in range(0, n):
        for j in range(h, information[i][0] - 1, -1):
            for k in range(t, information[i][1] - 1, -1):
                dp[j][k] = max(dp[j][k], dp[j-information[i][0]][k-information[i][1]] + information[i][2])
    print(dp[h][t])


if __name__ == '__main__':
    main()
