def main():
    n = int(input())
    information = [int(x) for x in input().split()]
    up_ends = []
    up_dp = [0 for _ in range(n)]
    down_ends = []
    down_dp = [0 for _ in range(n)]
    for i in range(n):
        up_left = 0
        up_right = len(up_ends) - 1
        up_ans = -1
        while up_left <= up_right:
            mid = (up_left + up_right) // 2
            if up_ends[mid] < information[i]:
                up_left = mid + 1
            else:
                up_right = mid - 1
                up_ans = mid
        if up_ans == -1:
            up_ends.append(information[i])
        else:
            up_ends[up_ans] = information[i]
        up_dp[i] = (i+1) - len(up_ends)
    for j in range(n-1, -1, -1):
        down_left = 0
        down_right = len(down_ends) - 1
        down_ans = -1
        while down_left <= down_right:
            mid = (down_left + down_right) // 2
            if down_ends[mid] < information[j]:
                down_left = mid + 1
            else:
                down_right = mid - 1
                down_ans = mid
        if down_ans == -1:
            down_ends.append(information[j])
        else:
            down_ends[down_ans] = information[j]
        down_dp[j] = (n-j) - len(down_ends)
    dp = [0 for _ in range(n)]
    for i in range(n):
        dp[i] = up_dp[i] + down_dp[i]
    print(min(dp))


if __name__ == '__main__':
    main()
