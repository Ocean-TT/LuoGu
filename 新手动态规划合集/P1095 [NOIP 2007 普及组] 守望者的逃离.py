def main():
    M, S, T = map(int, input().split())
    dp = [0 for x in range(T+10)]
    step = 1
    Judge = 1
    for i in range(1, T+1):
        if (S - dp[i - 1]) < 102 and M == 1:
            Judge = 0
        if M >= 10:
            dp[i] += dp[i-step]+60
            M -= 10
            step = 1
        else:
            if Judge != 0:
                M += 4
                step += 1
            dp[i] = dp[i-1] + 17
        if dp[i] > S:
            print("Yes")
            print(i)
            return
    print("No")
    print(dp[T])


if __name__ == '__main__':
    main()
