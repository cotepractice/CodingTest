#장르별 가장 많이 재생된 노래 "2개씩" 모으기
#노래는 고유 번호로 구분하고, 수록하는 기준은 아래와 같음
#1. 속한 노래가 많이 재생된 장르 먼저 수록
#2. 장르 내에서 많이 재생된 노래 먼저 수록
#3. 장르 내에서 재생 횟수가 같은 노래 중 고유 번호가 가장 낮은 노래 먼저 수록
from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    dict = defaultdict(list) #[장르재생횟수,해당하는노래인덱스1, ...]
    
    for i in range(len(genres)):
        if genres[i] not in dict:
            dict[genres[i]] = [plays[i],i]
        else:
            dict[genres[i]][0] += plays[i]
            dict[genres[i]].append(i)

    
    lst = []
    for k in dict:
        lst.append([dict[k][0],k])
    #1. 많이 재생된 장르
    lst.sort(reverse=True)
    #2. 많이 재생된 노래 (최대 2개)
    for l in lst:
        songs_lst = []
        songs = dict[l[1]][1:]

        for s_idx in songs:
            songs_lst.append([plays[s_idx],s_idx])
        songs_lst.sort(reverse=True)

        #한 곡만 존재하면 한 곡만 출력
        if len(songs_lst)==1:
            answer.append(songs_lst[0][1])
        else:
            idx1,idx2 = songs_lst[0][1],songs_lst[1][1]

            if plays[idx1]==plays[idx2]:
                answer.append(min(idx1,idx2))
                answer.append(max(idx1,idx2))
            else:
                answer.append(idx1)
                answer.append(idx2)
        
    
    return answer