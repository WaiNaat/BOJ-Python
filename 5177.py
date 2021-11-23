import sys
import re
input = sys.stdin.readline
print = sys.stdout.write

# input
K = int(input())
for i in range(K):
	# 문자열의 맨 앞이나 맨 뒤의 공백 유무는 관계없다.
	s1 = input().rstrip().lstrip()
	s2 = input().rstrip().lstrip()
	# 대소문자는 구별하지 않는다
	s1 = s1.upper()
	s2 = s2.upper()
	# 여는 괄호끼리는 구별하지 않는다
	s1 = re.sub('[\[{]', '(', s1)
	s2 = re.sub('[\[{]', '(', s2)
	# 닫는 괄호끼리는 구별하지 않는다
	s1 = re.sub('[\]}]', ')', s1)
	s2 = re.sub('[\]}]', ')', s2)
	# 쉼표와 세미콜론은 구별하지 않는다
	s1 = re.sub(',', ';', s1)
	s2 = re.sub(',', ';', s2)
	# 공백이 하나 이상이라면 공백의 크기는 관계없다
	s1 = re.sub('\s+', ' ', s1)
	s2 = re.sub('\s+', ' ', s2)
	# 특수 부호의 바로 앞이나 바로 뒤의 공백 유무는 관계없다
	s1 = re.sub('\s?\(\s?', '(', s1)
	s1 = re.sub('\s?\)\s?', ')', s1)
	s1 = re.sub('\s?\.\s?', '.', s1)
	s1 = re.sub('\s?;\s?', ';', s1)
	s1 = re.sub('\s?:\s?', ':', s1)
	s2 = re.sub('\s?\(\s?', '(', s2)
	s2 = re.sub('\s?\)\s?', ')', s2)
	s2 = re.sub('\s?\.\s?', '.', s2)
	s2 = re.sub('\s?;\s?', ';', s2)
	s2 = re.sub('\s?:\s?', ':', s2)

	sol = "equal" if s1 == s2 else "not equal"
	print("Data Set %d: %s\n\n" % (i+1, sol))