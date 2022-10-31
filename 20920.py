'''
dict 활용: 단어별로 등장한 횟수를 셈
이후 dict를 배열로 바꾸고 (등장횟수, 단어길이, 알파벳순) 우선순위로 정렬
'''
import sys
input = sys.stdin.readline

# input & process
N, M = map(int, input().split())
words = {}
for _ in range(N):
    word = input().rstrip()

    if len(word) < M:
        continue

    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

words = list(words.items())

words.sort(key = lambda x: (-x[1], -len(x[0]), x[0]))

# output
print('\n'.join(word[0] for word in words))