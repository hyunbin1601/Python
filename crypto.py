inputFile = open("./cipher.txt", 'r')
distance = int(input("Enter the distance value: "))
plainTxt = ""
while True:
    line = inputFile.readline()
    if line == "":
        break
    for i in range(len(line)):
        char = line[i]
        if char.isalpha():
            if char.isupper():
                plainTxt += chr((ord(char) - distance - 65) % 26 + 65)
            else:
                plainTxt += chr((ord(char) - distance - 97) % 26 + 97)
        else:
            plainTxt += char
inputFile.close()
print(plainTxt)
