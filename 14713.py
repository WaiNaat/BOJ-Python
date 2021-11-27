import sys
input = sys.stdin.readline

# class
'''
class Parrot
	says = 앵무새가 말할 문장
	cur = 지금 says[cur]의 단어를 말할 차례
	sLen = 앵무새가 말할 문장의 단어 수
'''
class Parrot:
	def __init__(self, sentence):
		self.says = sentence
		self.cur = 0
		self.sLen = len(sentence)

# input
n = int(input().rstrip())
parrots = [Parrot(input().split()) for _ in range(n)]
parrot_words = 0
L = input().split()
# process
isPossible = True
for word in L:
	found = False
	# 현재 단어를 말할 수 있는 앵무새가 있는지 확인
	for parrot in parrots:
		if parrot.cur < parrot.sLen and parrot.says[parrot.cur] == word:
			found = True
			parrot.cur += 1
			if parrot.cur == parrot.sLen: parrot_words += parrot.sLen
			break
	# 말하지 못하면 실패
	if not found:
		isPossible = False
		break
# 모든 앵무새가 다 말하고 돌아갔는데 문장을 제대로 받아적지 못했을 경우
if parrot_words != len(L): isPossible = False
# output
print("Possible") if isPossible else print("Impossible")