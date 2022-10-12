'''
max(N)=2000이니까 O(N^2)알고리즘 사용가능할듯?
dict에 주어진 수들을 저장:
	어떤 수가 몇 번 인덱스에 위치해 있는지
이중for문으로 찾은 두 수를 더한다
	만약 그게 dict에 있고 두 수가 아닌 수면 ok
'''
import sys
input = sys.stdin.readline

# input
N = int(input())
A = list(map(int, input().split()))

# process
numbers = {}
for i in range(N):
	val = A[i]
	if val not in numbers:
		numbers[val] = set([i])
	else:
		numbers[val].add(i)

cnt = 0
for i in range(N):
	for j in range(i+1, N):
		val = A[i] + A[j]
		
		if val in numbers and len(numbers[val]) > 0:
			leftovers = set()
			if i in numbers[val]:
				leftovers.add(i)
			if j in numbers[val]:
				leftovers.add(j)

			cnt += len(numbers[val]) - len(leftovers)
			numbers[val] = leftovers

# output
print(cnt)