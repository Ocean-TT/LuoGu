def main():
    information = []
    n = int(input())
    for _ in range(n):
        a, b, g, k = map(int, input().split())
        information.append([a, b, g, k])

    x, y = map(int, input().split())
    ans = -1

    for i in range(n):
        if information[i][0] <= x and information[i][1] <= y and x <= information[i][0] + information[i][2] and y <= information[i][1] + information[i][3]:
            ans = i + 1

    print(ans)

if __name__ == "__main__":
    main()
