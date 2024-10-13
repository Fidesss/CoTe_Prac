n = int(input())                        # 입력 1
val = list(map(int, input().split()))   # 입력 2
s = int(input())                        # 입력 3

for i in range(n):                      # 반복문 1
    max_val = max(val[i:i+s+1])         # 주어진 범위에서 최댓값 찾기
    max_idx = val.index(max_val)        # 최댓값의 인덱스 추출
    if s == 0:                          # s가 0이면 반복문 끝내기
        break
    while max_idx != i and s != 0:      # 반복문 2
        val[max_idx], val[max_idx-1] = val[max_idx-1], val[max_idx]
        s -= 1
        max_idx -= 1

print(*val)                             # unpacking후 출력
