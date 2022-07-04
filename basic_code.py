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
