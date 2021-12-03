from collections import deque

# input
N = int(input())
L = list(map(int, input().split()))

# process
# 1. 오름차순 정렬
L.sort()
# 2. 최종적으로 하나의 체인만 남을 때 까지 반복.
cnt = 0
total = len(L)
L = deque(L)
while total > 1:
# 2.1. 맨 앞 체인에서 고리 하나를 뺀다.
	L[0] -= 1
# 2.2. 그걸로 맨 뒤 체인 두 개를 연결한다.
	L.append(L.pop() + L.pop() + 1)
	total -= 1
	cnt += 1

	if L[0] == 0:
		L.popleft()
		total -= 1

# output
print(cnt)