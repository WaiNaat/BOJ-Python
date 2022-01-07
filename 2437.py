import sys
input = sys.stdin.readline

# input
N = int(input())
w = list(map(int, input().split()))

# process
# x개의 추로 표현할 수 있는 숫자 구간을 [0, a]라고 할 때,
# 무게가 b인 추가가 포함된 x+1개의 추로 표현할 수 있는 구간은 [0+b, a+b].
# 이 두 구간이 합쳐졌을 때 연속된 숫자가 나오냐 그렇지 않느냐를 판단.
measurable = [0, 0]
w.sort()

for i in range(N):
	new = [ measurable[0] + w[i], measurable[1] + w[i] ]
	if measurable[1] + 1 < new[0]:
		break
	else:
		measurable = [ measurable[0], new[1] ]

# output
print(measurable[1] + 1)