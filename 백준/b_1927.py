# 최소 힙
import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            pop = heapq.heappop(q)
            print(pop)
    else:
        heapq.heappush(q, x)