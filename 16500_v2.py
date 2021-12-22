### 시간 초과 ###

import sys
input = sys.stdin.readline
import re

# input
S = input().rstrip()
N = int(input())
A = [input().rstrip() for _ in range(N)]

# process
'''
정규 표현식을 이용
(A 안의 word)* == S 인가?
'''
re_A = "(" + "|".join(A) + ")*"
result = re.fullmatch(re_A, S)

# output
print(1) if result is not None else print(0)