'''
슬라이딩 윈도우

a의 개수를 센다.
>> 윈도우의 크기를 a의 개수로 한다.
윈도우 내에 a만 있다면 a가 모두 연속임
>> 윈도우 내에 b의 개수를 센다.
>> 그 b들과 윈도우 밖의 a들과 바꾸면 됨
윈도우를 이동시키면서 최솟값 확인
'''
import sys
input = sys.stdin.readline

# input
S = input().rstrip()

# process
# 윈도우 초기화
window_size = S.count('a')
b_cnt = 0
for i in range(window_size):
    if S[i] == 'b':
        b_cnt += 1
sol = b_cnt

# 윈도우 이동
start = 1
while start != 0:
    if S[start - 1] == 'b':
        b_cnt -= 1
    if S[(start + window_size - 1) % len(S)] == 'b':
        b_cnt += 1
    
    sol = min(b_cnt, sol)

    start = (start + 1) % len(S)

# output
print(sol)