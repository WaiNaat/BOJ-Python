# input
n = int(input())
a = tuple(map(int, input().split()))
# process
'''
i번째 칸까지 오는 데 필요한 최소 점프 횟수를 jump(i)라고 하면
jump(i + j) =
	jump(i) + 1  (1<=j<=a(i))
	jump(j)
	둘 중 작은 값.
'''
jump = [1001 for _ in range(n)]
jump[0] = 0

for i in range(n):
	for j in range(1, a[i] + 1):
		if i + j >= n: break
		if jump[i + j] > jump[i] + 1:
			jump[i + j] = jump[i] + 1
# output
print(jump[n - 1] if jump[n - 1] != 1001 else -1)