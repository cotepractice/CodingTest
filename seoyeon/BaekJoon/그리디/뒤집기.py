#백준 #1439 뒤집기
#그리디 문제

string = input()

prev = string[0]
cnt1 = 0
cnt2 = 0
for s in string:
    # if (prev == '-1'):
    #     prev = s
    #     continue
    if (s != prev and s == '0'):
        cnt1 += 1
        prev = s
        continue
    if (s != prev and s == '1'):
        cnt2 += 1
        prev = s
        continue

# if (cnt1 == 0 and cnt2 == 0):
#     print(0)
# else:
print(max(cnt1,cnt2))