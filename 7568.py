import sys
input = sys.stdin.readline

# input
N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]
# process & output
'''
각 사람 A에 대해 그 사람보다 덩치 큰 사람이 몇 명인지 구해서 출력.
max(N)=50 이므로 O(n^2) 완전탐색 알고리즘 사용 가능.
'''
for me in people:
	weight, height = me
	rank = 1
	for opponent in people:
		w2, h2 = opponent
		if weight < w2 and height < h2: 
			rank += 1
	print(rank, end=' ')