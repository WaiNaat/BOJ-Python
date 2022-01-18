import sys
input = sys.stdin.readline
# input
n, k = map(int, input().split())
friend = [int(input()) for _ in range(n)]
# process
'''
어차피 친구가 왔을 때는 난로가 켜져 있음.
친구가 없는 시간에 난로를 꺼야 함.
친구가 없는 시간이 가장 긴 구간에서 끈다.

난로를 단 한 번만 켠다고 할 때
마지막 친구 퇴장시간 - 첫 친구 방문시간
만큼 켜져 있음. 여기서 빼면 됨.

heater := 난로가 켜져 있는 시간.
alone := 혼자 있는 시간 구간의 배열.
'''
k -= 1 # 이미 첫 친구가 왔을 때 불을 켬.
heater = friend[n - 1] + 1 - friend[0]
alone = [friend[i] - friend[i-1] - 1 for i in range(1, n)]

alone.sort()
while k > 0 and alone:
	heater -= alone.pop()
	k -= 1
# output
print(heater)