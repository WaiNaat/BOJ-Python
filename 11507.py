# input
S = input()
# process
deck = {'P':set([]), 'K':set([]), 'H':set([]), 'T':set([])}
isSame = False
sLen = len(S)
for i in range(0, sLen, 3):
	color = S[i]
	val = int(S[i + 1 : i + 3])
	# 중복 카드 여부 검사
	if val in deck[color]:
		isSame = True
		break
	deck[color].add(val)
# output
if not isSame:
	print(13 - len(deck['P']), 13 - len(deck['K']), 13 - len(deck['H']), 13 - len(deck['T']))
else: print("GRESKA")