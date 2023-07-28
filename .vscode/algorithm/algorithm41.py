# 테스트케이스 마다 한줄에 하나씩 출력해야 한다.

# n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).

# 이때, 약수들은 오름차순으로 나열해야 한다.

# n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.

while True:
    a = []
    m = int(input())
    k = 0
    if m == -1:
        break
    else:
        n = 1
        if m == 1:
            print(str(m) + " = 1")
        else:
            while n < m:
                if m % n == 0:
                    a.append(n)
                n = n + 1
            for i in range(len(a)):
                k = k + a[i]
            if k == m:
            
                print(str(m) + " = ", end = '')
                for i in range(len(a)-1):
                    print(str(a[i]), end = ' + ')
                print(str(a[len(a)-1]))
            
            else:
                print(str(m) + " is NOT perfect.")
                
                
        