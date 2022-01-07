import sys
input = sys.stdin.readline

# input
# 꽃들의 피는 날, 지는 날을 받아 flowers에 저장함.
# 예) 1월 14일에 펴서 11월 2일에 지는 꽃 = [114, 1102]
N = int(input())
flowers = []
for i in range(N):
	flower_info = list(map(int, input().split()))
	flowers.append([flower_info[0]*100 + flower_info[1], flower_info[2]*100 + flower_info[3]])

# process
# 꽃들을 오름차순으로 정렬한다.
# bloom에도 피어 있는 꽃 중 지는 날이 가장 늦은 꽃을 고르는 작업을 반복.
sol = 0
i = 0
bloom = 301
fall = 0
pickFlower = False # bloom에도 피어 있는 꽃이 있으면 True

flowers.sort()

while i < N and bloom < 1201:
	while i < N and bloom >= flowers[i][0]:
		if flowers[i][1] > fall:
			fall = flowers[i][1]
			pickFlower = True
		i += 1
	if pickFlower:
		bloom = fall
		sol += 1
		pickFlower = False
	else:
		i += 1

# output
# 만약 11월 30일에 꽃이 피어 있지 않으면 조건에 맞는 꽃들이 없다는 뜻.
if fall < 1201:
	sol = 0
print(sol)