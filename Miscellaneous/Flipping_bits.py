def flippingBits(n):
    # Write your code here
    for i in range(0,32):
        n=n ^ (1<<i);
    return n
