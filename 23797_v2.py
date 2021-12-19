# input
S = input()

# process
''' 
said_K := "마지막에" K라고 말한 개구리 수
said_P := "마지막에" P라고 말한 개구리 수

현재 듣고 있는 소리에 대해
	들은 소리가 P이고 K라고 말한 개구리가 
		없으면 새로운 개구리 추가
		아니면 said_K의 개구리 하나를 said_P로 옮김
	들은 소리가 K면 반대로
'''
said_K = 0
said_P = 0

for sound in S:
	# 현재 듣는 소리가 P일 때
	if sound == 'P':
		if said_K == 0:
			said_P += 1
		else:
			said_K -= 1
			said_P += 1
	# 현재 듣는 소리가 K일 때
	else:
		if said_P == 0:
			said_K += 1
		else:
			said_P -= 1
			said_K += 1
			
# output
print(said_P + said_K)