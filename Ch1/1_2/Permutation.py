s1="abcdefg"
s2="cdefgab  "

def isPermutation(s1, s2):
    if len(s1)!= len(s2):
        return False
    return sorted(s1)==sorted(s2)

print isPermutation(s1,s2)    