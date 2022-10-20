'''
숫자가 20개니까 비트마스킹으로 풀어봄
'''
import sys
input = sys.stdin.readline

M = int(input())
S = 0
MAX = (1 << 22) - 1
for _ in range(M):
    cmd = input().split()

    if cmd[0][0] == 'r': #remove
        S &= MAX - (1 << int(cmd[1]))
    
    elif cmd[0][0] == 'c': #check
        print(1 if (S & 1 << int(cmd[1])) == 1 << int(cmd[1]) else 0)
    
    elif cmd[0][0] == 't': #toggle
        S ^= 1 << int(cmd[1])

    elif cmd[0][0] == 'e': #empty
        S = 0

    elif cmd[0] == 'add': 
        S |= 1 << int(cmd[1])

    else: #all
        S = MAX