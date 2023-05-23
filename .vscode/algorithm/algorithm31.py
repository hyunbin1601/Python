import heapq

def huffman(freq, label):   #frequency와 label을 전달받는다, freq와 label은 배열
    n = len(freq)
    h = []  #최소힙 만들기
    for i in range(n):
        heapq.heappush(h, (freq[i], label[i]))  #freq와 label이 쌍을 heap에다가 집어넣음
    
    for i in range(1, n):  #index를 1번부터 n번까지 시행한다
        e1 = heapq.heappop(h)    #h는 위에서 지정한 큐
        e2 = heapq.heappop(h)
        
        heapq.heappush(h, (e1[0] + e2[0], e1[1] + e2[1]))   #왜 e1[0]과 e1[1]을 고려해야 할깡...?
        print(e1, "+", e2)
        
    print(heapq.heappop(h))   
            

label = ['f', 'e', 'c', 'b', 'd', 'a']

freq = [5, 9, 12, 13, 16, 45]

huffman(freq, label)