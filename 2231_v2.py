# input
N = int(input())
# process
'''
max(N)=1,000,000이고 시간제한 2초이므로 O(n) 완전탐색 가능.
max(N)이 일곱 자리 숫자이고, 각 자릿수는 0~9까지밖에 없으므로 분해합이 생성자가 되려면
N-9*7 ~ N 사이에 있어야만 함.
'''
found = False
for i in range(max(N-63, 0), N):
	digits = tuple(map(int, list(str(i))))
	digitSum = i + sum(digits)
	if digitSum == N:
		found = i
		break
# output
print(found) if found else print(0)