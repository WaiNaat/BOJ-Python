# input
n = int(input())
chicken = list(map(int, input().split()))
k = int(input())
# process
'''
인원수대로 나눠서 정렬 따로 실행
'''
size = n // k
for i in range(0, n, size):
	chicken[i : i + size] = sorted(chicken[i : i + size])
# output
print(*chicken)