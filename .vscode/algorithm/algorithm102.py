n, m = map(int, input().split())

basket = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    tmp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = tmp
    
for i in range(len(basket)):
    print(basket[i], end=' ')