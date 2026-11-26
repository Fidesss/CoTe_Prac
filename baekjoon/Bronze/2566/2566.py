import sys

a= []

max_val = [0,1,1]

# 9x9 이차원 리스트 생성
for _ in range(9):
    a.append(list(map(int, sys.stdin.readline().split())))

for row_idx, row in enumerate(a):
    for col_idx, col in enumerate(row):
        # 최댓값에 들어가야하는거 [최댓값, 행 번호, 열 번호]
        if col > max_val[0]:
            max_val[0] = col
            max_val[1] = row_idx+1
            max_val[2] = col_idx+1

print(max_val[0])
print(max_val[1], max_val[2])