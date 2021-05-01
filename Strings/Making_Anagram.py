def makeAnagram(a, b):
    count=0
    for i in range(97, 123):
        ia = sum(letter == chr(i) for letter in a)
        ib = sum(letter == chr(i) for letter in b)
        count+=abs(ia-ib)
    return count
