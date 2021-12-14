# input
time, subject_num = map(int, input().split())
time *= 24
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# process
'''
effi[i] = (i, cnt) := 1시간당 i점을 얻을 수 있는 공부를 최대 cnt시간동안 할 수 있음

100점을 맞기 위한 1시간당 점수 효율을 구한다.
	예를 들어 기본점수가 80점이고, 시간당 효율이 9점인 과목은
	100점을 맞기 위해 3시간동안 시간마다 9, 9, 2 효율의 공부를 해야 한다.
이후 시간당 효율이 좋은 공부부터 하면 된다.
'''
base = 0
effi = [[i, 0] for i in range(101)]
for i in range(subject_num):
	a = A[i]
	b = B[i]
	base += a

	studyHr, loss = divmod(100 - a, b)
	effi[b][1] += studyHr
	effi[loss][1] += 1

effi.sort(key = lambda x: (-x[0], x[1]))

final_score = base
for e in effi:
	if time == 0: break
	score, hr = e
	if hr > time:
		hr = time
	final_score += score * hr
	time -= hr

# output
print(final_score)