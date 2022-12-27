from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect

input = sys.stdin.readline
istr = lambda: input().strip()
inum = lambda: int(input().strip())
imap = lambda: map(int,input().strip().split())
ilist = lambda: list(map(int, input().strip().split()))

sys.setrecursionlimit(1000000)
mod = 1000000007

def matrix(n, m):
    return [[0] * (m) for _ in range(n)]
  
h1, h2, h3, w1, w2, w3 = imap()

a_range = min(h1, w1)
e_range = min(h2, w2)
i_range = min(h3, w3)

a_pos = list(range(1, a_range-1))
e_pos = list(range(1, e_range-1))
i_pos = list(range(1, i_range-1))

ans = 0

for a in a_pos:
  for e in e_pos:
    for i in i_pos:
      b_range = min(h1-a, w2-e)
      if b_range < 2:
        continue
      b_pos = list(range(1, b_range))
      for b in b_pos:
        c = h1-a-b
        if c<1: continue
        h = w2-b-e
        if h<1: continue
        g = h3-h-i
        if g<1: continue
        d = w1-a-g
        if d<1: continue
        f = 13-d-e
        if f<1: continue
        ans += 1
      
print(ans)
