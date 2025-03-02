def solution(s, f, r, dp, day):



def main():
    N = int(input())
    a = [0 for _ in range(N)]
    dp = [0] * (N+1)
    for i in range(N):
        a.append(int(input()))
    front = 0
    rear = N-1
    solution(a, front, rear, dp, 1)
    # for i in range(1, N+1):
    #     dp[i] = min(dp[i-1]+a[front]*i, dp[i-1]+a[re
    #     # print(dp[N])ar]*i)
    #     if a[front] > a[rear]:
    #         rear -= 1
    #     else:
    #         front += 1


if __name__ == '__main__':
    main()

