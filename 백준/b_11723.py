# 집합

import sys
input = sys.stdin.readline

m = int(input())

S = set()

for _ in range(m):
    # print(S)
    cmd = input().strip().split()
    
    if cmd[0] == 'add':
        if int(cmd[1]) in S:
            continue
        else:
            S.add(int(cmd[1]))
            
    elif cmd[0] == 'remove':
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
        else:
            continue
        
    elif cmd[0] == 'check':
        print(1 if int(cmd[1]) in S else 0)
        
    elif cmd[0] == 'toggle':
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
        else:
            S.add(int(cmd[1]))
            
    elif cmd[0] == 'all':
        S = set(i for i in range(1, 21))
        # print(S)
        
    elif cmd[0] == 'empty':
        S = set()