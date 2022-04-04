'''
2^n개의 물병은 최종적으로 1개로 합쳐짐.
따라서 N을 이진수의 형태로 나타내면
물병을 안 사고 최대한 합쳤을 때의 물병 수를 알 수 있음.

거기서 더 줄이려면
가장 물이 조금 들어 있는 물병 두 개를 합치면 됨.
(당연히 물병도 사야 함)

N + x = 2^n이 되는 정수 x가 항상 존재하므로
답이 없는 경우는 없음.
'''

# input
N, K = map(int, input().split())

# process
# N을 이진수로 변환
N = bin(N)[2:]

# 현재 물병 개수 계산
bottle = []
for i in range(len(N)):
    if N[i] == '1':
        # 현재 보고 있는 '1'이 몇의 자리인지 저장
        bottle.append(len(N) - 1 - i)

# 물병이 많으면 가장 작은 물병 두 개 합침.
buy = 0
while len(bottle) > K:
    small_bottle = bottle.pop()
    large_bottle = bottle.pop()

    buy += 2 ** large_bottle - 2 ** small_bottle
    bottle.append(large_bottle + 1)

# output
print(buy)