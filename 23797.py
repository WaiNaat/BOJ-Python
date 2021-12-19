### 시간 초과 ###
'''
O(n^2) 알고리즘이 되겠냐?ㅋㅋ
'''

# input
S = list(input())

# process
'''
frog_said[i] := i번 개구리가 마지막으로 말한 말
frog_num := 개구리 수
ch := 현재 들리는 소리

frog_said의 i번째 개구리에 대해
	frog_said[i] != ch : 이 개구리가 우는 것
	frog_said[i] == ch : 이 개구리는 아님
'''
frog_said = []
frog_num = 0
for ch in S:
	found = False
	for i in range(frog_num):
		if ch == 'P' and frog_said[i] == 'K':
			frog_said[i] = 'P'
			found = True
			break
		elif ch == 'K' and frog_said[i] == 'P':
			frog_said[i] = 'K'
			found = True
			break
	if not found:
		frog_said.append(ch)
		frog_num += 1
			
# output
print(frog_num)