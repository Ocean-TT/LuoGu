import random


def quick(left, right, arr):
    if left >= right:
        return
    pivot = arr[random.randint(left, right)]
    less = left
    greater = right
    move = less
    while move <= greater:
        if arr[move] == pivot:
            move += 1
        elif arr[move] < pivot:
            temp = arr[less]
            arr[less] = arr[move]
            arr[move] = temp
            move += 1
            less += 1
        else:
            temp = arr[greater]
            arr[greater] = arr[move]
            arr[move] = temp
            greater -= 1
    quick(left, less-1, arr)
    quick(greater+1, right, arr)
    return arr


def main():
    N = int(input())
    arr = list(map(int, input().split()))
    quick(0, N-1, arr)
    print(' '.join(map(str, arr)))


if __name__ == '__main__':
    main()
