s1="Mr John Smith   "
str_lengh=13

def doURLify(s1, str_lengh):
    return s1[0:str_lengh].replace(' ','%20')
    
print doURLify(s1, str_lengh)