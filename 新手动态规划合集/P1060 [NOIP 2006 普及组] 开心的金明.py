def main():
    total , n = map(int,input().split())
    information = []
    dp = [0] * (total+1)
    for i in range(n):
        information.append(list(map(int,input().split())))
    for i in range(n):
        temp = total
        while temp > information[i][0]:
            dp[temp]=max(dp[temp],(information[i][1]*information[i][0])+dp[temp-information[i][0]])
            temp -= 1
    print(dp[total])

if __name__ == '__main__':
    main()