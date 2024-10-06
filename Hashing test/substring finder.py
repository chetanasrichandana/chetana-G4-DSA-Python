def substring_finder(s, k):
    substrings = set()
    for i in range(len(s) - k + 1):
        substring = s[i:i+k]
        substrings.add(substring)
    return substrings

s = "abcabc"
k = 3
print(substring_finder(s, k))  


