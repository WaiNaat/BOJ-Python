import sys
input = sys.stdin.readline

# input
N, _ = map(int, input().split())
line = [[] for _ in range(7)]
cnt = 0
for _ in range(N):
	i, fret = map(int, input().split())
# process
	'''
	줄별로 스택을 각각 만들어서
	해당 줄 스택에 지금 어느 프렛들을 누르고 있는지 저장
	지금 연주하려는 음을 손을 떼지 않고 연주할 수 있는지 계산
	'''
	if not line[i]:
		cnt += 1
		line[i].append(fret)
		continue
	if line[i][-1] < fret:
		line[i].append(fret)
		cnt += 1
	else:
		while line[i] and line[i][-1] > fret:
			line[i].pop()
			cnt += 1
		if line[i] and line[i][-1] == fret: continue
		line[i].append(fret)
		cnt += 1
# output
print(cnt)