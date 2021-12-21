# input
N = int(input())
# process
'''
max(N)=1,000,000이고 시간제한 2초이므로 O(n) 완전탐색 가능
'''
found = False
for i in range(N):
	digits = tuple(map(int, list(str(i))))
	digitSum = i + sum(digits)
	if digitSum == N:
		found = i
		break
# output
print(found) if found else print(0)