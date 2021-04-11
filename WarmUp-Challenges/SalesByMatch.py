#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
#Complexity is time:O(n) & space=O(n)
def sockMerchant(n, ar):
    leftSocks=[]
    pairSocks=[]
    pair=0
    for socks in ar:
        if socks not in leftSocks:
            leftSocks.append(socks)
        else:
            leftSocks.remove(socks)
            pairSocks.append(socks)

    return len(pairSocks)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
