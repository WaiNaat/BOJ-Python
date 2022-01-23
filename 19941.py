# input
n, k = map(int, input().split())
table = list(input())
# process
'''
왼쪽 사람부터 햄버거를 고르는데
본인이 먹을 수 있는 햄버거 중 가장 왼쪽의 햄버거를 먹음.
'''
cnt = 0
for i in range(n):
	if table[i] == 'P':
		for j in range(i - k, i + k + 1):
			if not 0 <= j < n: continue
			if table[j] == 'H':
				table[j] = None
				cnt += 1
				break
# output
print(cnt)