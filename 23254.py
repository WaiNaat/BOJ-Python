### 틀렸습니다 ###
'''
반례
100 3
90 90 90
9 9 9
'''

# input
time, subject_num = map(int, input().split())
time *= 24
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# process
'''
공부 효율이 높은 과목부터 공부하면 된다.
단, 100점 근처에서 1시간 공부했을 때 100점을 넘겨 손해보는 점수를 고려해야 한다.
'''
subject = list(zip(A, B))
subject.sort(key = lambda x: (-x[1], -x[0]))
final_score = 0
for i in range(subject_num):
	a = subject[i][0]
	b = subject[i][1]
	# 공부 시간 계산(남은 시간 부족할 경우 포함)
	studyHr = (100 - a) // b
	if studyHr > time:
		studyHr = time
	time -= studyHr
	# 점수 계산
	score = a + studyHr * b
	# 다음과목 공부 1시간보다 이번과목 공부 1시간이 더 효율적일 경우
	# 또는 마지막 과목인데 공부시간이 남았을 경우
	if i < subject_num and time > 0:
		if i == subject_num - 1 or 100 - score >= subject[i+1][1]:
			score = min(100, score + b)
			time -= 1
	final_score += score

# output
print(final_score)