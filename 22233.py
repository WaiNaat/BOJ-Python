'''
set 사용하는 문제
'''
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
keywords = set(input().strip() for _ in range(N))

# process
sol = []
for _ in range(M):
	post = input().rstrip().split(',')
	
	for keyword in post:
		if keyword in keywords:
			keywords.remove(keyword)
	
	sol.append(f'{len(keywords)}')

# output
print('\n'.join(sol))