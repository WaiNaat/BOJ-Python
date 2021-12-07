# input
N, K = map(int, input().split())

# process
'''
1. 쪽지들을 오름차순으로 정렬했다고 가정.
2. i번 쪽지를 1번 쪽지 바로 왼쪽으로 옮기면 i-1개의 그렇고 그런 사이 탄생.
3. 항상 그렇고 그런 사이가 가장 많이 생기는 쪽지를 옮김(0<i<=N && i<=K+1 인 i 중 최대).
   한 번 옮긴 쪽지 번호 이상의 쪽지 번호는 옮길 수 없음. (모순으로 증명 가능)
4. K := K - (i-1)
'''
moved = [0 for _ in range(N+1)]
left_1 = []
last = N

while K > 0:
	move = min(last, K + 1)
	left_1.append(move)
	last = move - 1
	moved[move] = 1
	K -= last

# output
if left_1:
	for n in left_1: print(n, end=' ')
for i in range(1, N+1):
	if moved[i] == 0: print(i, end=' ')