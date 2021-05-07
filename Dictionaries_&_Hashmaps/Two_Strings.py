def twoStrings(s1, s2):
    # Write your code here
    for i in s1:
        if i in s2:
            return "YES"
    return "NO"
