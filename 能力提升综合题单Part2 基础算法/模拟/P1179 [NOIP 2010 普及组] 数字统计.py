def main():
    L, R = map(int, input().split())
    count = 0
    for i in range(L, R + 1):
        for j in range(0, len(str(i))):
            if str(i)[j] == '2':
                count += 1
    print(count)


if __name__ == '__main__':
    main()
