# input
_ = input()
equation = input()
# process & output
'''
앞에서부터 순서대로 계산만 하면 되므로
operator stack의 size는 1, operand stack의 size는 2. 
	>> 스택을 사용할 필요조차 없음

앞에서부터 char 하나씩 읽어서
	숫자면 알파벳이 나올 때까지 이어붙여서 숫자를 만든다.
	알파벳이 나오면 멈추고 계산.
'''
operator = operand1 = operand2 = None
val = None
printed = False
for ch in equation:
	# 숫자
	if '0' <= ch <= '9':
		if val is None: val = int(ch)
		else: val = val * 10 + int(ch)
	# 글자
	else:
		# 만들어진 숫자가 있으면 operand에 저장
		if val is not None:
			if operand1 is None: operand1 = val
			else: operand2 = val
			val = None
		# binary operator 계산할 수 있으면 계산
		if operand2 is not None and operator is not None:
			if operator == 'S': operand1 -= operand2
			elif operator == 'M': operand1 *= operand2
			elif operator == 'U': 
				if operand1 < 0:
					operand1 = -(-operand1 // operand2)
				else: operand1 //= operand2
			elif operator == 'P': operand1 += operand2
			operand2 = None
			operator = None
		# 출력명령 있으면 출력
		if ch == 'C':
			print(operand1, end=' ')
			printed = True
			continue
		# operator 갱신
		operator = ch
		
if not printed: print("NO OUTPUT")