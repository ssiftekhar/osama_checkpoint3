
def to_camel_case(text): 
    text1 = '' 
    text1 += text[0].upper() 
    for i in range(1, len(text)): 
        if (text[i] == ' '): 
            text1 += text[i + 1].upper() 
            i += 1
        elif(text[i - 1] != ' '): 
            text1 += text[i]  
    print(text1)

print(to_camel_case('denne testen gikk ikke bra'))