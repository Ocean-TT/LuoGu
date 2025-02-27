def main():
    n = int(input())
    dp = [0] * (n+1)
    temp = 0
    information = []
    for i in range(n - 1):
        information.append(list(map(int, input().split())))
    for a in range(len(information)):
        i = a + 1
        j = i
        for b in range(len(information[a])):
            j += 1
            if dp[j] == 0:
                dp[j] = information[a][b]
            else:
                dp[j] = min(dp[j], information[a][b] + dp[i])
    print(dp[n])


if __name__ == '__main__':
    main()
