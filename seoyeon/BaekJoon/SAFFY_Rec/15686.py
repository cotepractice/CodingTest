#백준 #15686 치킨 배달

def dfs(idx,cnt):

    global min_ans

    if cnt == M:

        ans = 0

        for i in house: 
            distance = float("inf")
            for j in range(len(visited)):
                if visited[j]:
                    check_num = abs(i[0]-chicken[j][0])+abs(i[1]-chicken[j][1])
                    distance = min(distance,check_num) # 각 집에 대해 치킨 거리가 최소인 값을 구함
            ans +=distance
        min_ans = min(ans,min_ans)

        return

    for i in range(idx,len(chicken)):
        if not visited[i]:

            visited[i] = True
            dfs(i+1,cnt+1)
            visited[i]=False

# def dfs(idx,cnt):
#     global min_ans 
#     #종결조건
#     if cnt == M:
#         current_ans = 0

#         for i in house: #집마다
#             distance = float("inf")
#             for j in range(len(chicken)): #치킨집 확인
#                 if visited[j]==True:
#                     d = abs(i[0]-chicken[j][0])+abs(i[1]-chicken[j][1])
#                     distance = min(distance,d)
#             current_ans += distance
            
#             if current_ans<min_ans:
#                 #print("here")
#                 min_ans = current_ans

    for i in range(idx,len(chicken)):
        if visited[i]==False:
            visited[i]=True
            dfs(i+1,cnt+1)
            visited[i]=False


N,M = map(int,input().split()) #N:도시 크기,M:치킨집최대개수
city = [[-1 for _ in range(M)] for _ in range(N)] #0:빈칸,1:집,2:치킨집
house = []
chicken = [] #총 M개

for n in range(N):
    lst = list(map(int,input().split()))
    city[n] = lst

for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            house.append([i,j])
        elif city[i][j]==2:
            chicken.append([i,j])

visited = [False for _ in range(len(chicken))]

min_ans = float("inf")
dfs(0,0)

print(min_ans)