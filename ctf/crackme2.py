a='0+,0+#.\'9+*#\"+n~..49.>:='
b = []
k = 0
for i in a:
    c = ord(i)
    c = c ^ k
    c = c ^ 67
    c = chr(c)
    b.append(c)
    k = k + 1
    
print(b)

n = []
n.append(chr((int('0x1a', 16) ^ 6) ^ 67))
n.append(chr((int('0x0c', 16) ^ 16) ^ 67))
n.append(chr((int('0x19', 16) ^ 17) ^ 67))
n.append(chr((int('0x14', 16) ^ 20) ^ 67))

print(n)


