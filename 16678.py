import sys
input = sys.stdin.readline
# input
n = int(input())
honors = [int(input()) for _ in range(n)]
# process
'''
명예점수 오름차순 정렬.

모독으로 모든 국회의원의 명예점수를 1 깎는다.
해커를 고용해서 가장 명예가 낮은 의원의 점수를 0으로 만든다.
반복.
'''
insult = 1 # 처음 defile 시작시 1회 모독
hacker = 0
honors.sort()
for honor in honors:
	# honor-insult<0 이면 이미 예전에 박탈당했단 뜻.
	if honor - insult >= 0:
		hacker += honor - insult
		insult += 1
# output
print(hacker)