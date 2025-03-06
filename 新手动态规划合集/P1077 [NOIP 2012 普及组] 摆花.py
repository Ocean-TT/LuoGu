def dfs(k, t, n, m, information, dp):
    ans = 0
    if t == m:
        return 1
    if t > m:
        return 0
    if dp[k][t] != 0:
        return dp[k][t]
    if k == n:
        return 0
    for i in range(0, information[k]+1):
        ans += dfs(k+1, t+i, n, m, information, dp)
    dp[k][t] = ans
    return ans % 1000007


def main():
    n, m = map(int, input().split())
    information = [int(x) for x in input().split()]
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    print(dfs(0, 0, n, m, information, dp))


if __name__ == '__main__':
    main()
