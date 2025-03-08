def dfs(left, right, s, dp):
    if dp[left][right] != 0:
        return dp[left][right]
    if left == right:
        return 0
    if s[left] == s[right]:
        dp[left][right] = dfs(left + 1, right - 1, s, dp)
    else:
        dp[left][right] = min(dfs(left + 1, right, s, dp), dfs(left, right - 1, s, dp)) + 1
    return dp[left][right]


def main():
    S = str(input())
    dp = [[0 for _ in range(len(S))] for _ in range(len(S))]
    n = len(S)
    for i in range(n):
        dp[i][i] = 0
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if S[i] == S[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j]+1, dp[i][j-1]+1)
    print(dp[0][len(S)-1])


if __name__ == '__main__':
    main()
