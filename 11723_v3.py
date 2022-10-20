'''
set으로 풀어봄
'''
import sys
input = sys.stdin.readline

M = int(input())
S = set()
base = [i for i in range(1, 21)]

for _ in range(M):
    cmd = input().split()

    if cmd[0][0] == 'r': #remove
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
    
    elif cmd[0][0] == 'c': #check
        print(1 if int(cmd[1]) in S else 0)
    
    elif cmd[0][0] == 't': #toggle
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
        else:
            S.add(int(cmd[1]))

    elif cmd[0][0] == 'e': #empty
        S = set()

    elif cmd[0] == 'add': 
        S.add(int(cmd[1]))

    else: #all
        S = set(base)