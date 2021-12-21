import sys
input = sys.stdin.readline

# input
T = int(input())
for _ in range(T):
	word = list(input().rstrip())
# process
	'''
	word의 i번째 알파벳 ch에 대해...
		ch 뒤의 알파벳들이 다 자기보다 (사전 순으로) 빨라야 함
			>> 이러면 ch와 그 뒤의 알파벳들 중 하나를 교환했을 때 word보다 빨라져서 교환 불가능.
		느린 알파벳이 있다?
			그러면 느린 알파벳 중 가장 빠른 녀석과 ch를 교환.
			이후 i번째 알파벳 뒤쪽의 알파벳들을 정렬.
	
	사전 순으로 바로 다음 단어를 구하는 거라 i는 오름차순이 아니라 내림차순으로 변화.
	max(len(word))=100, max(T)=10 이므로 O(n^2) 알고리즘 사용 가능.
	'''
	for i in range(len(word) - 2, -1, -1):
		ch = word[i]
		slower_fastest = None
		slower_fastest_idx = -1

		for j in range(i+1, len(word)):
			candidate = word[j]
			if ch < candidate: # ch보다 느림
				if slower_fastest_idx == -1 or slower_fastest > candidate: # s느린 애들 중 가장 빠름
					slower_fastest_idx = j
					slower_fastest = candidate
		
		if slower_fastest is not None:
			word[i], word[slower_fastest_idx] = word[slower_fastest_idx], word[i]
			word[i + 1 :] = sorted(word[i + 1 :])
			break
# output
	print("".join(word))