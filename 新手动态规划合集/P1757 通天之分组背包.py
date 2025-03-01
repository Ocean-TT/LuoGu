def main():
    m, n = map(int, input().split())
    group = []
    k = 0
    dp = [0] * (m+1)
    for i in range(n):
        w, v, d = map(int, input().split())
        if k != d:
            k += 1
        if k >= len(group):
            group.extend([[] for _ in range(k-len(group) + 1)])
        group[k].append([w, v])
    for i in range(1, len(group), +1):
        for j in range(m, -1, -1):
            for k in range(len(group[i])):
                if j >= group[i][k][0]:
                    dp[j] = max(dp[j], dp[j - group[i][k][0]] + group[i][k][1])
    print(dp[m])


if __name__ == '__main__':
    main()
