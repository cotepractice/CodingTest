#백준 #1475 방 번호
#구현 문제

numbers = input()

my_card = [0 for _ in range(10)]

order = True
for i in numbers:
    i = int(i)

    if (i == 6 or i == 9):
        if (order == True):
            my_card[6] += 1
            order = False
        else:
            my_card[9] += 1
            order = True
    else:
        my_card[i] += 1
print(max(my_card))