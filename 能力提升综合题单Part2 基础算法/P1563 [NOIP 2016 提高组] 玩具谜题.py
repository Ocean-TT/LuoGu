def main():
    n, m = map(int, input().split())
    ans = 1
    Circle = [[0, 'sign'] for _ in range(n + 2)]
    for i in range(1, n + 1):
        Circle[i][0], Circle[i][1] = input().split()
        Circle[i][0] = int(Circle[i][0])
    Command = [[0, 0] for _ in range(m + 1)]
    for i in range(1, m + 1):
        Command[i][0], Command[i][1] = map(int, input().split())
    for i in range(1, m + 1):
        if (Circle[ans][0] == 0 and Command[i][0] == 0) or (Command[i][0] == 1 and Circle[ans][0] == 1):
            ans -= Command[i][1]
        else:
            ans += Command[i][1]
        if ans < 1:
            ans = n + ans
        if ans > n:
            ans = ans - n
    print(Circle[ans][1])


if __name__ == '__main__':
    main()
