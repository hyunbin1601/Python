a='{aexdmWkzikcem+9WCmaK`ga'
b = []
for i in a:
    c = ord(i)
    c = c ^ 8
    c = chr(c)
    b.append(c)
    
print(b)
