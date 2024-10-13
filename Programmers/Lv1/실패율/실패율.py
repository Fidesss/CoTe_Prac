def solution(N, stages):
    challenger = [0] * (N+2)
    for stage in stages:                            # 각 스테이지에 도전하는 사람들을 저장하는 리스트
        challenger[stage] += 1
    
    fails = {}                                      # 실패율을 딕셔너리에 저장
    total = len(stages)                             # 스테이지에 도전하는 전체 사람 수
    
    for i in range(1, N+1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]
    
    answer = sorted(fails, key = lambda x : fails[x], reverse = True)
    return answer