import sys

a = []
result =""

# 입력
for _ in range(5):
    # split을 안하고 list 자체로 캐스팅하면 알아서 요소가 나눠진다.
    a.append(list(sys.stdin.readline().rstrip()))

# 모든 각각의 위치에 맞게 리스트에 넣어서 출력하면 되지 않을까?
for col in range(15):
    for row in range(15):
        if col < len(a[row]):
            result += a[row][col]

print(result)