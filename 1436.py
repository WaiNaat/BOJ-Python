import re
# input
N = int(input())
# process
'''
무식하게 666부터 +1씩 하면서 종말의 수면 cnt++
'''
val = '666'
cnt = 1
while cnt < N:
	val = str(int(val) + 1)
	if re.fullmatch("\d*666\d*", val) is not None:
		cnt += 1
# output
print(val)

'''
이게 되네ㅋㅋ
'''