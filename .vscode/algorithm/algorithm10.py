#단어의 개수를 세고, 이를 반환하여 출력하는 문제

def WordNumber(voca):
    wordnumber = voca.split()   #split()메소드는 문자열을 공백으로 분리하고, 분리된 문자열을 리스트로 리턴함
    return len(wordnumber)

n= input()
print(WordNumber(n))