def substrCount(n, s):
    l = []
    count = 0
    cur = None

    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
        print(l)
    l.append((cur, count))
    print(l)
    ans = 0
        
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2
        print("ans:",ans)

    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])
            print(l[i - 1][1], l[i + 1][1])
            print(ans)

    return ans
