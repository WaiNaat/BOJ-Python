'''
스택 사용
1. 탑을 주어진 순서대로 스택에 넣음
2. 넣기 전에, 스택 꼭대기가 본인보다 작으면 전파수신X -> 스택에서 제거
3. 만약 스택이 비었으면 본인의 신호를 받을 수 있는 탑이 없음
스택에는 (높이, 본인번호)를 저장
'''
import sys
input = sys.stdin.readline

# input
N = int(input())
towers = map(int, input().split())

# process
stack = []
sol = []

i = 0
for tower in towers:
	i += 1

	while stack and stack[-1][0] < tower:
		stack.pop()
	
	if not stack:
		sol.append('0')
	else:
		sol.append(str(stack[-1][1]))

	stack.append((tower, i))

# output
print(' '.join(sol))