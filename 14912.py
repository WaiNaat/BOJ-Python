# input
n, d = input().split()
# process
'''
max(n)=100,000
최대 6자리 숫자이므로
각 자리에 어떤 숫자가 있는지 세는 건 문제X
따라서 O(n) 완전탐색 사용 가능
'''
cnt = 0
n = int(n) + 1
for i in range(1, n):
	cnt += str(i).count(d)
# output
print(cnt)