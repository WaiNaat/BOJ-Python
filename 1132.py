import sys
input = sys.stdin.readline
# input
n = int(input())
alphabet = [0 for _ in range(10)]
notZero = set()
for _ in range(n):
	num = input().rstrip()
# process
	'''
	각 숫자가 입력될 때마다
	각 알파벳이 몇의 자리인지 계산해서 반영
	가장 자리수가 큰 알파벳부터 9를 받음.
	
	0을 쓸 수 있는 애들 중 가장 작은 애가 0을 받음.
	'''
	notZero.add(ord(num[0]) - ord('A'))
	for i in range(len(num)):
		alphabet[ord(num[i]) - ord('A')] += pow(10, len(num) - 1 - i)

alphabet = list(zip(alphabet, [i for i in range(10)]))
alphabet.sort()
for val, ch in alphabet:
	if ch not in notZero:
		alphabet.remove((val, ch))
		alphabet.insert(0, (val, ch))
		break

sol = 0
for i in range(10):
	sol += i * alphabet[i][0]
# output
print(sol)