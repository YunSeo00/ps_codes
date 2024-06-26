# 최단 경로 (다익스트라)

import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance[k] = 0
q = []
heapq.heappush(q, (0, k))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = distance[now] + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

for i in range(1, v+1):
    print(distance[i] if distance[i] < INF else 'INF')