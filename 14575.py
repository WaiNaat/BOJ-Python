import sys
input = sys.stdin.readline
# function
def drink(s, alcohol):
	'''
	이미 L만큼 마신 사람들에게 alcohol만큼의 술을
	min(s, 본인주량)을 넘지 않는 선에서 분배하고 남은 술을 반환.
	'''
	for person in LR:
		limit = min(s, person[1])
		if person[0] < limit: 
			alcohol -= limit - person[0]
			if alcohol <= 0: break
	return alcohol

# input
N, T = map(int, input().split())
LR = []
sum_L = sum_R = 0
left = right = 1
for _ in range(N):
	L, R = map(int, input().split())
	LR.append((L, R))
	sum_L += L
	sum_R += R
	if left < L: left = L
	if right < R: right = R
# process
'''
일단 모든 사람이 적어도 마셔야 하는 술의 합을 sum(L)이라 하면
그만큼 마시고 나머지인 T - sum(L)을 분배하는 문제.
이 값이 음수면 애초에 술이 모자란 것.

또한 모든 사람이 술을 최대로 마셨을 때 sum(R)만큼 마신다 하면
만약 T - sum(R) > 0 이면 애초에 T만큼의 술을 마실 수 없음.

분배 방식은 한명씩 붙잡아서 min(S, 본인주량) 채울때까지 먹이기.
만약 이렇게 분배하고도 남은 술의 양 k가
k > 0: S를 늘린다.
k = 0: S를 줄인다.
'''
alcohol_left = T - sum_L
S = -1
isPossible = True if alcohol_left >= 0 and T - sum_R <= 0 else False
if isPossible:
	# left값 시작은 L값이 가장 큰 사람임
	# right값 시작은 R값이 가장 큰 사람임
	right += 1
	while left < right:
		mid = (left + right) // 2
		if drink(mid, alcohol_left) > 0: left = mid + 1
		else: right = mid
	S = left
# output
print(S)