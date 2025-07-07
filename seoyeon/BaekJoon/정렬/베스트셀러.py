#백준 #1302 베스트셀러
#정렬문제
#리스트 미리 정의해 메모리 초과 해결

#1. 메모리 초과
# import sys

# input = sys.stdin.readline

# n = int(input())

# books = []

# for _ in range(n):
#     book = input().rstrip()

#     if (books == []):
#         books.append([int(1), book])
#     else:
#         for i in range(len(books)):
#             if (book == books[i][1]):
#                 books[i][0] += 1
#             else:
#                 books.append([int(1), book])
# books.sort(reverse=True)
# result = []
# for i in range(len(books)):
#     if (i == 0):
#         result.append(books[0][1])
#         continue
#     if (books[i][0] == books[0][0]):
#         result.append(books[i][1])

# result.sort()
# print(result[0])

#2. 메모리 초과 해결하기 위해 모든 list를 필요한 index만큼 미리 정의
import sys

input = sys.stdin.readline

n = int(input())

books = [[0,0] for _ in range(n)]

for k in range(n):
    book = input().rstrip()

    if (k == 0):
        books[0] = [int(1), book]
        idx = 1
        continue
    check = 0
    for i in range(idx):
        #print(book, books[i][1], book== books[i][1])
        if (book == books[i][1]):
            #print("same")
            books[i][0] += 1
            check = 1
            break
    if (check == 0):
        books[idx] = [int(1), book]
        idx += 1
    #print("books",books)

#print(books)
books.sort(key=lambda x:x[0], reverse=True)
result = ['z'*51 for _ in range(len(books))]
for i in range(len(books)):
    if (i == 0):
        result[i] = books[0][1]
        continue
    if (books[i][0] == books[0][0]):
        result[i] = books[i][1]

result.sort()
print(result[0])