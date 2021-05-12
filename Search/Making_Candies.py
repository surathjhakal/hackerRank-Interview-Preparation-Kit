def minimumPasses(m, w, p, n):
    # Write your code here
    if n <= p: return math.ceil(n / (m * w))

    curr = candy = 0
    ans = 10**12
    while candy < n:
        if candy < p:
            i = math.ceil((p - candy) / (m * w))
            print(i)
            curr += i
            candy += m * w * i
            continue

        buy,candy = divmod(candy , p)
        # print(buy,candy)
        total = m + w + buy
        half = total // 2
        # print("half",half)
        if m > w :
            m = max(m, half)
            w = total - m
        else:
            w = max(w, half)
            m = total - w

        curr += 1
        candy += m * w
        ans = min(ans, curr + math.ceil((n - candy) / (m * w)))

    return min(ans, curr)
