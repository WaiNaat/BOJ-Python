# input
n, k = map(int, input().split())
wheel = input()
# process
wheel = list(wheel)
if n > 1:
	for _ in range(k):
		aux = [None for _ in range(n)]
		for i in range(n):
			# 자기 주변 index 파악
			rCnt = gCnt = bCnt = 0
			lookAt = [i-1, i, i+1]
			if i == 0: lookAt = [0, 1, n-1]
			elif i == n-1: lookAt = [n-2, n-1, 0]
			# 자기 주변 색깔 확인
			for j in lookAt:
				if wheel[j] == 'R': rCnt += 1
				elif wheel[j] == 'G': gCnt += 1
				else: bCnt += 1
			# 조건에 맞춰서 칠함
			if rCnt == gCnt == bCnt == 1 or rCnt == 3 or gCnt == 3 or bCnt == 3:
				aux[i] = 'B'
			elif (rCnt == 2 and gCnt == 1) or (gCnt == 2 and bCnt == 1) or (bCnt == 2 and rCnt == 1):
				aux[i] = 'R'
			else:
				aux[i] = 'G'
		# 1회 변경 완료
		wheel = aux
else:
	wheel = ["G"]
wheel = "".join(wheel)
# output
print(wheel.count('R'), wheel.count('G'), wheel.count('B'))