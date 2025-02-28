def main():
    V = int(input())
    n = int(input())
    information = [0]
    dp = [V] * (V+1)
    for i in range(n):
        information.append(int(input()))
    for i in range(1, n + 1, +1):
        for j in range(V, -1, -1):
            if j >= information[i]:
                dp[j] = min(dp[j], dp[j-information[i]] - information[i])
    print(dp[V])

if __name__ == '__main__':
    main()
