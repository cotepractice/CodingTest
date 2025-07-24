# def solution(answers):
#     sol1 = [1,2,3,4,5]  #5개
#     sol2 = [2,1,2,3,2,4,2,5]    #8개
#     sol3 = [3,3,1,1,2,2,4,4,5,5]    #10개
    
#     n = len(answers)
    
#     answer1 = sol1*(n//5 +1)
#     answer2 = sol2*(n//8 +1)
#     answer3 = sol3*(n//10 +1)
    
#     sol = [0,0,0]
    
#     for i in range(n):
#         if (answers[i] == answer1[i]):
#             sol[0] += 1
#         if (answers[i] == answer2[i]):
#             sol[1] += 1
#         if (answers[i] == answer3[i]):
#             sol[2] += 1
    
#     idx = 0
#     answer = []
#     for k in range(3):
#         if (k == 0):
#             answer.append(k+1)
#         elif (sol[k] > sol[idx]):
#             idx = k
#             answer = []
#             answer.append(k+1)
#         elif (sol[k] == sol[idx]):
#             answer.append(k+1)
    
#     return answer

def solution(answers):
    N = len(answers) #전체 문제 수
    
    #수포자
    p1,p2,p3 = [],[],[]
    
    p2_next = [1,3,4,5]
    p2_index = 0
    p3_next = [3,3,1,1,2,2,4,4,5,5]
    p3_index = 0
    for i in range(1,N+1):
        #수포자1
        p1_next = i%5
        if p1_next==0:
            p1.append(5)
        else:
            p1.append(p1_next)
        
        #수포자2
        if i%2==1:
            p2.append(2)
        else:
            p2.append(p2_next[p2_index])
            if p2_index==3:
                p2_index=0
            else:
                p2_index += 1
        #수포자3
        p3.append(p3_next[p3_index])
        if p3_index==9:
            p3_index=0
        else:
            p3_index+=1

    result = [0,0,0] #p1,p2,p3
    
    #각 수포자 점수 체크
    for i in range(N):
        if p1[i]==answers[i]:
            result[0]+=1
        if p2[i]==answers[i]:
            result[1]+=1
        if p3[i]==answers[i]:
            result[2]+=1
    
    #가장 높은 점수 가진 사람 계산
    max_ans = 0        
    ans = []
    for r in range(3):
        if result[r]>max_ans:
            max_ans=result[r]
            ans=[r+1]
        elif result[r]==max_ans:
            ans.append(r+1)
    
    return ans