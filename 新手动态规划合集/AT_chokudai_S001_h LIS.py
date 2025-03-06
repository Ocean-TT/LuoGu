def main():
    n = int(input())
    information = [int(x) for x in input().split()]
    ends = []
    for i in range(n):
        left = 0
        right = len(ends) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if ends[mid] < information[i]:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        if ans == -1:
            ends.append(information[i])
        else:
            ends[ans] = information[i]
    print(len(ends))


if __name__ == '__main__':
    main()
