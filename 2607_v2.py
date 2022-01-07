import sys
input = sys.stdin.readline

n = int(input())

# 첫 번째 단어의 구성 파악
first = input().rstrip()
letter1 = [0 for _ in range(26)]
for ch in first: letter1[ord(ch) - 65] += 1

sol = 0
for _ in range(n-1):
	word = input().rstrip()
	# 글자 길이가 두 개 이상 차이나면 볼 필요 없이 아님.
	if abs(len(first) - len(word)) > 1: continue
	# 비교할 단어의 구성 파악
	letter2 = [0 for _ in range(26)]
	for ch in word: letter2[ord(ch) - 65] += 1

	# 1. 길이가 같을 경우 구성이 똑같거나 한 글자만 달라야 함
	if len(first) == len(word):
		if ''.join(list(map(str, letter1))) == ''.join(list(map(str, letter2))):
			sol += 1
		else:
			for i in range(26):
				if letter1[i] > 0:
					tmp = letter1.copy()
					tmp[i] -= 1
					for j in range(26):
						temp = tmp.copy()
						temp[j] += 1
						if ''.join(list(map(str, temp))) == ''.join(list(map(str, letter2))):
							sol += 1
							break
					
	# 2. 첫 번째 단어가 한 글자 더 길 경우
	# 첫 번째 단어에서 하나를 뺀 구성이랑 같은지 검사
	elif len(first) > len(word):
		for i in range(26):
			if letter1[i] > 0:
				temp = letter1.copy()
				temp[i] -= 1
				if ''.join(list(map(str, temp))) == ''.join(list(map(str, letter2))):
					sol += 1
					break
	# 3. 비교할 단어가 한 글자 더 길 경우
	# 비교할 단어에서 하나를 뺀 구성이랑 같은지 검사
	else:
		for i in range(26):
			if letter2[i] > 0:
				temp = letter2.copy()
				temp[i] -= 1
				if ''.join(list(map(str, temp))) == ''.join(list(map(str, letter1))):
					sol += 1
					break

print(sol)