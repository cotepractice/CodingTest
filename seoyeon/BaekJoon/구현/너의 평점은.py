#백준 #25206 너의 평점은
#구현

score = 0
scoreAndGrade = 0

for i in range(20):
    grade = 0

    a,b,c = list(input().split())

    if (c=="A+"):
        grade += 4.5
        score += float(b)
    elif (c=="A0"):
        grade += 4.0
        score += float(b)
    elif (c=="B+"):
        grade += 3.5
        score += float(b)
    elif (c=="B0"):
        grade += 3.0
        score += float(b)
    elif (c=="C+"):
        grade += 2.5
        score += float(b)
    elif (c=="C0"):
        grade += 2.0
        score += float(b)
    elif (c=="D+"):
        grade += 1.5
        score += float(b)
    elif (c=="D0"):
        grade += 1.0
        score += float(b)
    elif (c=="F"):
        grade += 0.0
        score += float(b)

    scoreAndGrade += float(b) * grade
    
# print("%.6f" % (scoreAndGrade/score))
print(format(scoreAndGrade/score, ".6f"))