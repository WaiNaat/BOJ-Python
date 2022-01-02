# input
s = input()
# process
'''
1부터 하나씩 보면서
입력 맨 앞의 숫자가 나오면 그걸 지운다.
입력의 숫자가 모두 지워질 때까지 반복.
'''
s_idx = num = 0
while s_idx != len(s):
	num += 1
	for ch in str(num):
		if s_idx < len(s) and s[s_idx] == ch:
			s_idx += 1
# output
print(num)