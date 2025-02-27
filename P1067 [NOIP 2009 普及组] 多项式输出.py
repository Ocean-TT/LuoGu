def main():
    n = int(input())
    first_term = True

    for i in range(n, -1, -1):  # 注意，循环要从大到小
        x = int(input())
        if x != 0:
            if not first_term and x > 0:
                print('+', end='')
            if i != 0 and x == -1:
                print('-', end='')
            if abs(x) > 1 or i == 0:
                print(x, end='')
            if i > 1:
                print(f"x^{i}", end='')
            elif i == 1:
                print('x', end='')
            first_term = False

    print()  # 输出换行符


if __name__ == "__main__":
    main()
