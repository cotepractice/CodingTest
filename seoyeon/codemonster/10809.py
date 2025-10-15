import string

S = input()

answer = []
s_dict=dict()
for idx,s in enumerate(S):
    if s not in s_dict:
        s_dict[s]=idx

for alpha in string.ascii_lowercase:
    if alpha in s_dict:
        answer.append(s_dict[alpha])
    else:
        answer.append(-1)
print(*answer)