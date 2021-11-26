import sys
input = sys.stdin.readline
print = sys.stdout.write

# INPUT
n, m = map(int, input().split())
words = []
wLen = 0
for _ in range(n):
	word = input().rstrip()
	wLen += len(word)
	words.append(word)

# PROCESS & OUTPUT
# 필요한 밑줄의 개수 구하기
# base : 최소한 단어와 단어 사이엔 이 개수만큼의 밑줄이 필요
# add_ : 만약 딱 나누어 떨어지지 않으면 이 값들을 적절히 나눠서 분배해야 함
_num = m - wLen
base = _num // (n - 1)
base = ''.join(['_' for _ in range(base)])
add_ = _num % (n - 1)
# 출력
# 일단 첫 번째 단어 출력
print(words[0])
prev = cur = words[0][0].isupper()
case_changed = not cur
# 나머지 출력
for i in range(1, n):
	# 밑줄 출력
	print(base)
	cur = words[i][0].isupper()
	# 대문자 < 밑줄 < 소문자 순서
	# 대문자 => 소문자로 바뀌면 밑줄이 많을수록 유리
	if prev and not cur: case_changed = True
	# 소문자 => 대문자로 바뀌면 밑줄이 적을수록 유리
	elif not prev and cur: case_changed = False
	# 밑줄이 많을수록 유리하거나 남은 단어가 적어서 추가 밑줄을 반드시 넣어야 할 때
	if case_changed or i >= n - add_:
		if add_ > 0:
			print('_')
			add_ -= 1
	print(words[i])
	prev = cur