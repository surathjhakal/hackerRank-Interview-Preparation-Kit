#!/bin/python3
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
