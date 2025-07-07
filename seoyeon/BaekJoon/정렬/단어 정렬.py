#백준 #1181 단어 정렬
#정렬 문제
#1:09-1:23

n = int(input())

words = ['' for _ in range(n)]
length = [0 for _ in range(n)]

for i in range(n):
    word = input()
    words[i] = word
    length[i] = len(word)

result = []

for j in range(51):     #문자열의 길이가 50을 넘지 않으므로 51까지로 설정
    sortedByLength = [] #1. 문자열 길이가 짧은 순으로 
    for i in range(n):
        if (length[i] == j):
            if (words[i] not in sortedByLength):
                sortedByLength.append(words[i])
    sortedByLength.sort()   #2. 문자열의 길이가 같은 경우 사전 순으로
    #print("sorted",sortedByLength)
    for k in range(len(sortedByLength)):
        result.append(sortedByLength[k])
    #print("result",result)

print(*result, sep="\n")