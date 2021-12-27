# functions
def binarySearch(val, left, right):
	if left > right: return 0

	mid = (left + right) // 2

	if val == A[mid]: return 1
	elif val < A[mid]: return binarySearch(val, left, mid -1)
	else: return binarySearch(val, mid + 1, right)

# input
N = int(input())
A = list(map(int, input().split()))
M = int(input())
X = tuple(map(int, input().split()))
# process & output
A.sort()
for x in X: print(binarySearch(x, 0, N - 1))