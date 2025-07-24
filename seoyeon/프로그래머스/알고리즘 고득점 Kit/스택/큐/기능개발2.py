# #progress:작업진도 ,speeds:개발속도
# def solution(progresses, speeds):
#     answer = []
    
#     end_time = [0 for _ in range(len(progresses))]
    
#     for i in range(len(progresses)):
#         if (100-progresses[i])%speeds[i]==0:
#             end_time[i]=(100-progresses[i])//speeds[i]
#         else:
#             end_time[i]=(100-progresses[i])//speeds[i] + 1
#     print(end_time)     
#     visited=[False for _ in range(len(progresses))]
#     for i in range(len(progresses)):
#         if visited[i]==True:
#             continue

#         start = i
#         ans = 1
#         for j in range(i+1,len(progresses)):
#             if end_time[j]<=end_time[start]:
#                 ans += 1
#                 visited[j]=True
#             else:
#                 break
#         answer.append(ans)
        
#     return answer

#완전탐색
def solution(progresses, speeds):
    
    ans = [] #ans = [[n,day],[n,day]] #n:기능 개수, day: 날짜
    prev = 0
    
    for i in range(len(progresses)):
        #day: i번째 작업을 처리하는데 필요한 날짜
        day = (100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i]!=0:
            day += 1
        
        if i==0:
            ans.append([1,day])
        elif ans[prev][1]>=day:
            ans[prev][0] += 1
        else:
            ans.append([1,day])
            prev += 1
    
    result = []
    for x,y in ans:
        result.append(x)
    
    return result