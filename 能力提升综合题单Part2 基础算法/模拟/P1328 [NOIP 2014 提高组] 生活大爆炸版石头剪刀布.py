def main():
    N, NA, NB = map(int, input().split())
    A_score = B_score = 0
    table = [[0, 2, 1, 1, 2],
             [1, 0, 2, 1, 2],
             [2, 1, 0, 2, 1],
             [2, 2, 1, 0, 1],
             [1, 1, 2, 2, 0]]
    A_Queue = [int(x) for x in input().split()]
    while len(A_Queue) < N:
        A_Queue.append(A_Queue[len(A_Queue) - NA])
    B_Queue = [int(y) for y in input().split()]
    while len(B_Queue) < N:
        B_Queue.append(B_Queue[len(B_Queue) - NB])
    for i in range(N):
        if table[A_Queue[i]][B_Queue[i]] == 1:
            A_score += 1
        elif table[A_Queue[i]][B_Queue[i]] == 2:
            B_score += 1
    print(A_score, B_score)


if __name__ == '__main__':
    main()
