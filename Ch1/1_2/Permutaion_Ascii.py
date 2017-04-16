s1="abcdefg "
s2="defg abc"

def isPermutation_ascii(s1,s2):
    if len(s1)!=len(s2):
        return False
    checkArray=[0]*128
    for i in range(len(s1)):
        asciiVal=ord(s1[i])
        checkArray[asciiVal]+=1
        
    for j in range(len(s2)):
        asciiVal=ord(s2[j])
        checkArray[asciiVal]-=1
        if checkArray[asciiVal]<0:
            return False
    return True
print isPermutation_ascii(s1, s2)
