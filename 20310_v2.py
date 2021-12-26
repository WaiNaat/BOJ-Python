# input
s = input()
# process
'''
타노스한 결과 S 안의 문자들의 순서가 뒤섞여서는 안 된다.

타노스한 결과가 사전 순으로 앞서기 위해선
결과의 앞쪽에 0이 최대한 많고,
결과의 뒤쪽에 1이 최대한 많아야 한다.

따라서 앞에서부터 읽으면서 1을 지우고,
뒤에서부터 읽으면서 0을 지운다.
'''
# 타노스할 개수 계산.
cnt0 = cnt1 = 1
for ch in s:
	if ch == '0': cnt0 += 1
	else: cnt1 += 1
cnt0 //= 2
cnt1 //= 2
# 1 타노스
s = s.replace('1', '', cnt1)
# 0 타노스
s = s[::-1]
s = s.replace('0', '', cnt0)
s = s[::-1]
# output
print(s)