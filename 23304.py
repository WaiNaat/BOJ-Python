'''
1. 본인이 팰린드롬인지 확인
2. 접두사도 팰린드롬인지 확인

이걸 계속 재귀하면 됨
'''
import sys

# function
def is_akaraka(length):
    # base case
    if length == 1:
        return True
    
    # recursive step
    left = 0
    right = length - 1
    while left < right:
        if S[left] != S[right]:
            return False
        left += 1
        right -= 1
    
    return is_akaraka(int(length / 2))
    

# input
S = sys.stdin.readline().rstrip()

# process & output
print('AKARAKA' if is_akaraka(len(S)) else 'IPSELENTI')