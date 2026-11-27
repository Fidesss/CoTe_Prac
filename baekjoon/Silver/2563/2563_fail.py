import sys

# 처음 input을 통해 몇 번의 input을 더 받을지 결정 (0일 경우 생각)
input_num = int(sys.stdin.readline())

a = []
delta = 10


for i in range(input_num):
    a.append(list(map(int, sys.stdin.readline().split())))

# 만약 두 색종이면 차이를 10에서 빼야된다.
# 각 색종이의 가로 값과 세로 값의 차이를 절댓값으로 구한 후 각각 10에서 빼고 넓이를 구해서 총 넓이에서 뺀다.
# 각각의 가로, 세로의 차가 10 초과면 검사하지 않고 이하면 검사하고 이런식
# 차가 10이 아닌건 확인했는데 이걸 어떻게 하나하나씩 판별?
# a는 이중리스트고

total = len(a) * 100

# 넓이 접근 식 실패
for idx in range(len(a)):
    # if idx+1 == len(a):
    #     break
    for j in range(idx+1, len(a)):
        width = 0
        height = 0
        if abs(a[idx][0] - a[j][0]) < delta and abs(a[idx][1] - a[j][1]) < delta:
            width = abs(a[idx][0] - a[j][0])
            height = abs(a[idx][1] - a[j][1])
            total -= (10 -width) * (10 - height)
print(total)