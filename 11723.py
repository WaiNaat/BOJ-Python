'''
배열로 해당 원소가 있는지 없는지 확인
'''
import sys
input = sys.stdin.readline

M = int(input())
S = [False for _ in range(21)]

for _ in range(M):
    cmd = input().split()

    if cmd[0][0] == 'r': #remove
        S[int(cmd[1])] = False
    
    elif cmd[0][0] == 'c': #check
        print(1 if S[int(cmd[1])] else 0)
    
    elif cmd[0][0] == 't': #toggle
        S[int(cmd[1])] = not S[int(cmd[1])]

    elif cmd[0][0] == 'e': #empty
        S = [False for _ in range(21)]

    elif cmd[0] == 'add': 
        S[int(cmd[1])] = True

    else: #all
        S = [True for _ in range(21)]