s="abcde!!"

def is_unique(s):
    if len(s)>128: return False
    
    booleanArray=[False]*128
    
    for i in range(len(s)):
        asciiVal= ord(s[i])
        if booleanArray[asciiVal]:
            return False
        booleanArray[asciiVal]=True
    
    return True
        
if __name__ == "__main__":
    print is_unique(s)  
    
    