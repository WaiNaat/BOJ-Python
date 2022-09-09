import sys
input = sys.stdin.readline

T = int(input())
test_case = [map(int, input().split()) for _ in range(T)]

sol = []
for a, b in test_case:
	# 규칙 찾기
	pc = a % 10
	seq = [pc]
	pc = (pc * a) % 10
	while seq[0] != pc:
		seq.append(pc)
		pc = (pc * a) % 10
		
	# 계산
	val = str(seq[(b - 1) % len(seq)])
	sol.append(val if val != '0' else '10')

print('\n'.join(sol))