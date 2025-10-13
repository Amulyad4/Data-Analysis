def prelettercase(s, letter):
    index = s.lower().find(letter.lower())  
    
    if index == -1:  
        return s.lower()
    elif index == 0:  
        return s.upper()
    else:
        return s[:index].lower() + s[index:].upper()
    
print(prelettercase("cAptcHeR","p"))
