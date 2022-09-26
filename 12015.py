'''
일단 이 방법은 아님 왜? 시간이 단 1초라서 O(N^2)알고리즘은 못통과할게 뻔함
	opt(i) := i를 마지막으로 하는 가장긴증가하는부분수열 의 길이
	opt(i) = opt(k) + 1
		k는 i보다 작으면서 A(k) < A(i)

이분탐색라는데 그럼 뭘 움직여야하지? 감도안잡히는데

자리뺏기 https://st-lab.tistory.com/285
이미 만들어진 가긴증부수가 있고, 현재 보고 있는 수를 A(i)라 할 때
A(i)가 가긴증부수 뒤에 붙을 수 없다면
이분탐색으로 가긴증부수에서 A(i) 초과인 숫자중에서 가장 작은숫자의 자리를 뺏는다.

이렇게 하면 현재까지 가장 긴 가긴증부수의 길이는 유지를 하면서(뻇은 자리 이후부터는 순서가 깨지지만 길이는 그대로)
혹시 모를 더 긴 가긴증부수를 대비할 수 있다 (가긴증부수에서 처음~A(i)까지는 정상적이기 때문)
'''
import sys
input = sys.stdin.readline

# function
def findpos(arr, val):
	left = 0
	right = len(arr)

	while left < right:
		mid = int((left + right) / 2)

		if arr[mid] < val:
			left = mid + 1
		else:
			right = mid

	return left

# input
N = int(input())
A = tuple(map(int, input().split()))

# process
arr = [A[0]]

for val in A:
	if arr[-1] < val:
		arr.append(val)
	else:
		pos = findpos(arr, val)
		arr[pos] = val

# output
print(len(arr))