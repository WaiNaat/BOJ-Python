# input
p_num, dest = map(int, input().split())
P = list(map(int, input().split()))
X = list(map(int, input().split()))

# process
'''
현솔이가 지금 p_i 지점의 인력거를 탔을 때,
그 다음엔 [p_i, p_i + x_i] 사이 지점의 인력거꾼 중 가장 멀리 가는 사람 걸로 갈아타면 된다.
위 구간에 인력거꾼이 없으면 환승 불가.

cur_finish := 현재 인력거 최대 이동 위치
next_finish_max := 환승 시 인력거 최대 이동 위치
next_start := 환승 인력거 출발지점
next_finish := 환승 인력거 최대 이동 위치
'''
cnt = 0
cur_finish = P[0] + X[0]
next_finish_max = cur_finish
found = False

i = 1
while i < p_num:
	# 도착 시
	if cur_finish >= dest:
		break
	
	next_start = P[i]
	next_finish = next_start + X[i]
	# 환승 가능한 인력거인지 확인
	while next_start <= cur_finish:
	# 환승 가능한 인력거 중 가장 멀리 가는 녀석
		if next_finish > next_finish_max:
			next_finish_max = next_finish
			found = True
	# 다음 인력거
		i += 1
		if i >= p_num: break
		next_start = P[i]
		next_finish = next_start + X[i]
	# 환승 가능한 인력거 없음
	if not found:
		break
	# 환승
	cur_finish = next_finish_max
	cnt += 1
	found = False

if cur_finish < dest:
	cnt = -1

# output
print(cnt)