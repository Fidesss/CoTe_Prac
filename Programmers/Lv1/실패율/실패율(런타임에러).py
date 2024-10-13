def solution(N, stages):
    fail_list = []
    answer = []
    Num = len(stages)
    for i in range(1, N+1):
        sum = 0
        for j in stages:
            if i == j:
                sum += 1
        else:
            fail_list.append([i, sum/Num])
            Num -= sum

    fail_list.sort(key = lambda x : x[1])
    fail_list.reverse()
    
    for x in range(1, len(fail_list)+1):
        if x == len(fail_list):
            break
        elif fail_list[x][1] == fail_list[x-1][1] and fail_list[x-1][0] > fail_list[x][0]:
            fail_list[x-1][0], fail_list[x][0] =  fail_list[x][0], fail_list[x-1][0]
        for x in range(1, len(fail_list)+1):
            if x == len(fail_list):
                break
            elif fail_list[x][1] == fail_list[x-1][1] and fail_list[x-1][0] > fail_list[x][0]:
                fail_list[x-1][0], fail_list[x][0] =  fail_list[x][0], fail_list[x-1][0]
            
    
    for y in fail_list:
        answer.append(y[0])
    
    return answer

num1 = 4
stages = [4,4,4,4,4]
print(solution(num1,stages))