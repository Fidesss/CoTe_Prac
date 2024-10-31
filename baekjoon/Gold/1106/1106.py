C, N = map(int, input().split())
cities=[[0,0]]
for i in range(N):
    line= list(map(int, input().split()))
    cities.append(line)

maxCost = float('INF')
dp= [maxCost for _ in range(C+100)]
dp[0]=0

for i in range(1, N+1):
    cost = cities[i][0]
    val = cities[i][1]
    
    for j in range(val, C+100):    
        dp[j] = min(dp[j], dp[j-val]+cost)
        
print(min(dp[C:]))