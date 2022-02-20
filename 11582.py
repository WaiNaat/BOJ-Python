import sys
sys.setrecursionlimit(10 ** 6)
# function
def mergeSort(start, size):
	# base case
	if size == 1:
		return
	# recursive step
	# 반으로 갈라서 재귀
	size //= 2
	mergeSort(start, size)
	mergeSort(start + size, size)
	# 왼쪽과 오른쪽을 병합
	aux = []
	leftIdx = start
	rightIdx = start + size
	while leftIdx < start + size and rightIdx < start + size * 2:
		if chicken[leftIdx] < chicken[rightIdx]:
			aux.append(chicken[leftIdx])
			leftIdx += 1
		else:
			aux.append(chicken[rightIdx])
			rightIdx += 1
	while leftIdx < start + size:
		aux.append(chicken[leftIdx])
		leftIdx += 1
	while rightIdx < start + size * 2:
		aux.append(chicken[rightIdx])
		rightIdx += 1
	chicken[start : start + size * 2] = aux
	
# input
n = int(input())
chicken = list(map(int, input().split()))
k = int(input())
# process
'''
인원수대로 나눠서 병합정렬 따로 실행
'''
size = n // k
for i in range(0, n, size):
	mergeSort(i, size)
# output
print(*chicken)