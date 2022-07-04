N = int(input())
As = list(map(int, input().split()))
sum = 0
P = 0
for i in range(N):
  sum += As[N-1-i]
  if sum >= 4:
    P += 1
print(P)