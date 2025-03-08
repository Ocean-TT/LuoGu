def main():
    N = int(input())
    dp = [[0 for i in range(N)] for j in range(N)]
    dp[0][N//2] = 1
    rem = [0, N//2]
    for i in range(2, N*N+1):
        if rem[0] == 0 and rem[1] != N-1:
            dp[N-1][rem[1]+1] = i
            rem = [N-1, rem[1]+1]
            continue
        if rem[0] != 0 and rem[1] == N-1:
            dp[rem[0]-1][0] = i
            rem = [rem[0]-1, 0]
            continue
        if rem[0] == 0 and rem[1] == N-1:
            dp[1][N-1] = i
            rem = [1, N-1]
            continue
        if rem[0] != 0 and rem[1] != N-1:
            if dp[rem[0]-1][rem[1]+1] == 0:
                dp[rem[0]-1][rem[1]+1] = i
                rem = [rem[0]-1, rem[1]+1]
            else:
                dp[rem[0]+1][rem[1]] = i
                rem = [rem[0]+1, rem[1]]
            continue
    for x in dp:
        for y in x:
            print(y, end=" ")
        print()


if __name__ == '__main__':
    main()
