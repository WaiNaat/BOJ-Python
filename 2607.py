### 틀렸습니다 ###

import sys
import copy
input = sys.stdin.readline

n = int(input())

# 첫 번째 단어의 구성 파악
first = input().rstrip()
ch1 = {}
for ch in first:
    if ch in ch1: ch1[ch][0] += 1
    else: ch1[ch] = [1, 0]

sol = 0
for _ in range(n-1):
    word = input().rstrip()
    # 새로운 단어의 글자수가 첫 단어보다 2개 이상 적거나 많으면 무시
    if len(word) < len(first)-1 or len(word) > len(first)+1 : continue
    # 새로운 단어의 구성 파악
    ch2 = copy.deepcopy(ch1)
    for ch in word:
        if ch in ch2: ch2[ch][1] += 1
        else: ch2[ch] = [0, 1]
    # 새로운 단어가 얼마나 비슷한지 파악
    diffCnt = 0
    chngCnt = 0
    isSim = True
    for ch in ch2:
        if ch2[ch][0] == 0:
            if ch2[ch][1] < 2: diffCnt += 1
            else: isSim = False
        elif abs(ch2[ch][0] - ch2[ch][1]) > 1: isSim = False
        elif abs(ch2[ch][0] - ch2[ch][1]) == 1: chngCnt += 1
    if isSim and chngCnt < 2 and diffCnt < 2:
        sol += 1

print(sol)