'''
슬라이딩 윈도우
'''
import sys
input = sys.stdin.readline

# input
N, X = map(int, input().split())
visitors = tuple(map(int, input().split()))

# process
visitor_sum = 0
for i in range(X):
    visitor_sum += visitors[i]

max_visitors = visitor_sum
max_cnt = 1

for i in range(X, N):

    visitor_sum -= visitors[i - X]
    visitor_sum += visitors[i]

    if visitor_sum > max_visitors:
        max_visitors = visitor_sum
        max_cnt = 1
    elif visitor_sum == max_visitors:
        max_cnt += 1

# output
print(f'{max_visitors}\n{max_cnt}' if max_visitors > 0 else 'SAD')