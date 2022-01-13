import sys
input = sys.stdin.readline
# input
n, k, q, m = map(int, input().split())
sleep = set(map(int, input().split()))
code = set(map(int, input().split()))
interval = [map(int, input().split()) for _ in range(m)]

# process
'''
길이 n의 배열을 이용해서 해당 번호 학생의 출첵 실패 여부를 구함.

이후 그 배열을 해당 학생이 출첵했는지가 아니라
해당 학생을 포함한 이전 번호의 학생들 중 출첵 실패한 학생 수로 변환.
>> max(N)=5,000이라 금방 함.

구간별로 출첵 실패한 학생의 수는 구간합으로 구함.
'''
code -= sleep # 자는 애들은 코드 못 보냄
check_failed = [1 for _ in range(n + 3)]
check_failed[0] = check_failed[1] = check_failed[2] = 0
for c in code:
	for i in range(c, n + 3, c):
		check_failed[i] = 0
for s in sleep:
	check_failed[s] = 1

for i in range(3, n + 3):
	check_failed[i] += check_failed[i - 1]

sol = []
for left, right in interval:
	sol.append(check_failed[right] - check_failed[left - 1])
	
# output
print(*sol, sep='\n')