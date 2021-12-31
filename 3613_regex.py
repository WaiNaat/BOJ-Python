import re
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
	>> 근데 소문자로만 된 건 그대로 출력.
'''
isJava = isCpp = False
if re.fullmatch("[a-z][A-Za-z]*", var) is not None: isJava = True
if re.fullmatch("[a-z](_?[a-z])*", var) is not None: isCpp = True
result = []
if isJava and not isCpp:
	for ch in var:
		if 'A' <= ch <= 'Z': result.append("_%s" % ch.lower())
		else: result.append(ch)
elif isCpp and not isJava:
	next2Upper = False
	for i in range(len(var)):
		ch = var[i]
		if ch == '_': next2Upper = True
		else:
			if next2Upper is True:
				ch = ch.upper()
				next2Upper = False
			result.append(ch)
elif re.fullmatch("[a-z]*", var) is not None: result = var
else: result.append("Error!")
# output
print("".join(result))