### 미완성 코드(틀렸습니다) ###

import sys
input = sys.stdin.readline
# function
def backtrack(idx):
	if idx == len(word): return
	if word[idx - 1] < word[idx]:
		backtrack(idx + 1)
	elif word[idx - 1] < word[idx][::-1]:
		word[idx] = word[idx][::-1]
		reversed[idx] = '1'
		backtrack(idx + 1)
	
	return
# input
t = int(input())
for _ in range(t):
	n = int(input())
	word = [input().rstrip() for _ in range(n)]
# process
	'''
	백트래킹을 위해서는 어떤 그래프를 만들 필요가 있음.
	정점간의 연결?
	기본적으로 나와 내 다음 단어는 연결되어 있음.
	만약 내 다음 단어가 나보다 빠르면?
	나를 뒤집거나 내 다음 단어를 뒤집어야 함.
	그러면 그 연결 관계는 나-내 다음이 아니라
	나-뒤집힌 다음 또는 뒤집힌 나-다음 의 관계로 바뀜.
	몰?루
	'''
	reversed = ['0' for _ in range(n)]
	backtrack(0)
# output
	print("".join(reversed))