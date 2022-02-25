# function
def dfs(m):
	if len(seq) == m:
		print(*seq)
		return
	
	for num in numbers:
		seq.append(num)
		dfs(m)
		seq.pop()

# input
n, m = map(int, input().split())
numbers = map(int, input().split())

# process & output
'''
같은 수를 여러 번 골라도 된다.
즉 n개의 자연수들 중에서 중복이 있든 없든 상관이 없다.
[4, 4, 2] 이거랑 [4, 2] 이거랑 결과물이 같을 수밖에 없음.
>> 입력을 set으로 변환해서 중복값 제거
'''
numbers = sorted(list(set(numbers)))
seq = []
dfs(m)