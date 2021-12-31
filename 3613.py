# input
var = input()
# process
'''
앞에서부터 하나씩 읽으면서 처리.
만약 첫번째 알파벳이 대문자면 잘못된 변수명.
중간에 대문자가 나올 경우 자바임.
	>> 밑줄 추가하고 소문자로 바꿔줌.
중간에 밑줄이 나올 경우 cpp임.
	>> 밑줄 지우고 다음 단어 대문자로 바꿈.
	>> 밑줄이 두 번 연속으로 나오면 잘못된 변수명.
	>> 마지막 글자가 밑줄이면 잘못된 변수명.
만약 자바와 cpp 조건 둘 다 만족하면 잘못된 변수명.
'''
isJava = isCpp = next2Upper = False
isValid = True
result = [var[0]]
if 'A' <= var[0] <= 'Z' or var[0] == '_': isValid = False
for i in range(1, len(var)):
	ch = var[i]
	if 'A' <= ch <= 'Z':
		isJava = True
		result.append('_%s' % ch.lower())
		if isCpp: isValid = False
	elif ch == '_':
		if next2Upper: isValid = False
		next2Upper = isCpp = True
		if isJava: isValid = False
	else:
		if next2Upper:
			ch = ch.upper()
			next2Upper = False
		result.append(ch)
	if not isValid: break
if next2Upper: isValid = False
# output
print("".join(result)) if isValid else print("Error!")