# input
N = int(input())
L = list(map(int, input().split()))

# process
# 1. 오름차순 정렬
L.sort()
# 2. 최종적으로 하나의 체인만 남을 때 까지 반복.
cnt = first = 0
while N > 1:
# 2.1. 맨 앞 체인에서 고리 하나를 뺀다.
	L[first] -= 1
	if L[first] == 0:
		N -= 1
		first += 1
# 2.2. 그걸로 맨 뒤 체인 두 개를 연결한다. 결과적으로 체인 총 개수는 하나가 줄어든다.
	N -= 1
	cnt += 1

# output
print(cnt)