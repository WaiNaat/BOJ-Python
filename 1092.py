# input
n = int(input())
crane_limit = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
# process
'''
물건과 크레인을 각각 내림차순/오름차순으로 정렬.
크레인에게 물건을 분배하는 기준:
	그 물건을 감당할 수 있는 크레인 중
	분배받은 물건의 양이 가장 적은 크레인.
'''
crane_limit.sort()
box.sort(reverse=True)

sol = -1
# 가장 무거운 물건을 가장 힘 센 크레인이 못 들 경우 애초에 불가능
if box[0] <= crane_limit[-1]:
	crane = [0 for _ in range(n)]
	for b in box:
		# 물건을 감당할 수 있는 크레인들 계산
		crane_idx = n - 1
		while crane_idx > 0 and crane_limit[crane_idx - 1] >= b:
			crane_idx -= 1
		# 분배받은 물건이 가장 적은 크레인에게 분배.
		min_idx = min_val = 1000001
		for i in range(crane_idx, n):
			if crane[i] < min_val:
				min_idx = i
				min_val = crane[i]
		crane[min_idx] += 1
	sol = max(crane)

# output
print(sol)