import sys
input = sys.stdin.readline
# input
N = int(input())
options = [list(input().rstrip()) for _ in range(N)]
# process
'''
어떤 옵션 O에 대해
	1. O를 이루는 단어의 첫 알파벳이 단축키로 지정되어 있는지 검사.
	2. O의 첫 알파벳부터 단축키가 될 수 있는게 있는지 검사.

shortcuts := 단축키를 소문자로 저장하는 집합.
'''
shortcuts = set([])
for option in options:
	# 1.
	found = False
	wordStart = True
	for i in range(len(option)):
		# 단어의 첫 알파벳이 단축키로 지정되어 있는지 확인.
		if wordStart:
			if option[i].lower() not in shortcuts:
				shortcuts.add(option[i].lower())
				option[i] = "[%s]" % option[i]
				found = True
				break
			wordStart = False
		# 공백 다음에 나오는 알파벳은 단어의 시작.
		elif option[i] == ' ':
			wordStart = True
	# 2.
	if not found:
		for i in range(len(option)):
			# 공백은 무시
			if option[i] == ' ': continue
			# 단축키가 될 수 있는지 검사.
			if option[i].lower() not in shortcuts:
				shortcuts.add(option[i].lower())
				option[i] = "[%s]" % option[i]
				break
# output
	print("".join(option))