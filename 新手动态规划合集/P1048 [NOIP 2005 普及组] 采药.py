def main():
    T, M = map(int, input().split())
    dp = [0] * (T + 1)
    information = []
    for i in range(M):
        information.append(list(map(int, input().split())))
    for i in range(1, M + 1, +1):
        for j in range(T, -1, -1):
            if j >= information[i - 1][0]:
                dp[j] = max(dp[j], dp[j - information[i-1][0]] + information[i - 1][1])
    print(dp[T])


if __name__ == '__main__':
    main()
