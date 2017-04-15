s="abcde"

#so it first and check neighbor if it's same
def isUnique_inspace(s):
    
    sortedString=''.join(sorted(s))
    for i in range(len(s)-1):
        if sortedString[i]==sortedString[i+1]:return False
    return True

if __name__ == "__main__":
    print isUnique_inspace(s)
