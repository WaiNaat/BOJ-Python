from collections import deque

# input
_ = input()
equation = input()

# process & output
'''
deque 사용
입력값 훑으면서 숫자는 operand queue에, 글자는 operator stack에 right push
이후 left pop하면서 차례대로 계산, 결과는 다시 left push
'''
operand_deque = deque([])
operator_deque = deque([])
digits = []
for ch in equation:
	# 숫자
	if '0' <= ch <= '9':
		digits.append(ch)
	# 글자
	else:
		# 숫자 만들어야 할 게 있으면 만들고 operand deque에 저장
		if digits:
			val = int("".join(digits))
			digits = []
			operand_deque.append(val)
		# operator deque에 저장
		operator_deque.append(ch)
# 계산
printed = False
while operator_deque:
	operator = operator_deque.popleft()
	if operator == 'C':
		print(operand_deque[0], end=' ')
		printed = True
		continue
	if len(operand_deque) < 2: continue
	o1, o2 = operand_deque.popleft(), operand_deque.popleft()
	if operator == 'S':
		operand_deque.appendleft(o1 - o2)
	elif operator == 'M':
		operand_deque.appendleft(o1 * o2)
	elif operator == 'U':
		if o1 < 0: operand_deque.appendleft(-(-o1 // o2))
		else: operand_deque.appendleft(o1 // o2)
	else: # 'P'
		operand_deque.appendleft(o1 + o2)

if not printed: print("NO OUTPUT")