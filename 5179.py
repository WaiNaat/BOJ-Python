import sys
input = sys.stdin.readline
# input
k = int(input())
for test in range(1, k + 1):
	prob_num, try_num, parti_num = map(int, input().split())
	p_try = [{} for _ in range(parti_num + 1)]
	p_score = [[0, 0, i] for i in range(parti_num + 1)]
	p_correct = [set() for _ in range(parti_num + 1)]
	for _ in range(try_num):
		p, prob, time, isCorrect = input().split()
		p, time, isCorrect = map(int, (p, time, isCorrect))
# process
		'''
		참가자별로 문제 트라이 횟수를 세는 dict.
		문제를 맞췄을 경우 해당 참가자의 점수 +.
		참가자별로 문제 맞은 개수도 기억해야 함.
		참가자별로 맞은 문제 번호도 기억해야 함.

		p_try[i] := i번 참가자의 각 문제별 틀린 횟수를 저장.
					key:문제번호, value:틀린횟수.
		p_score[i] := i번 참가자의 결과를 저장하는 배열.
					[0]맞은문제수 [1]점수 [2]참가번호
		p_correct[i] := i번 참가자가 맞은 문제 번호의 집합.
		'''
		# 틀렸으면 해당 참가자의 시도 횟수에 추가.
		if not isCorrect:
			if prob not in p_try[p]: p_try[p][prob] = 0
			p_try[p][prob] += 1
		# 맞았는데 이미 맞은 문제일 경우.
		elif prob in p_correct[p]: continue
		# 문제를 맞힌 경우
		else:
			p_score[p][0] += 1
			try_score = 0 if prob not in p_try[p] else p_try[p][prob] * 20
			p_score[p][1] += time + try_score
			p_correct[p].add(prob)
	# 순위대로 정렬
	# 참가자 번호를 내림차순으로 정렬해야 맨 마지막이 가상의 0번 참가자가 됨.
	p_score.sort(key = lambda x: (-x[0], x[1], -x[2]))
# output
	print(f"Data Set {test}:")
	for p in p_score[:len(p_score) - 1]: print(p[2], p[0], p[1])
	print()