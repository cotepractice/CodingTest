sentence = list(input())

dp = [0 for _ in range(len(sentence)+1)]

prev_stick = 0
prev_lazer = False
for s in range(len(sentence)-1):
    if prev_lazer:
        prev_lazer=False
        continue
    if sentence[s]=="(" and sentence[s+1]==")":
        dp[s] = prev_stick
        prev_lazer=True
        continue
    elif sentence[s]=="(":
        prev_stick += 1
        dp[s]=1
    elif sentence[s]==")":
        prev_stick -= 1

answer = 0
for i in range(len(dp)):
    answer += dp[i]
print(answer)
