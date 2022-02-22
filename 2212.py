# input
n = int(input())
k = int(input())
sensor = map(int, input().split())
# process
'''
센서들의 좌표를 정렬
각 센서마다 본인 다음 센서와의 거리를 계산
거리들 정렬
가장 긴 거리 제거
	>> 처음에는 하나였던 센서들이 두 개의 묶음으로 쪼개짐
	>> 두 개의 집중국
다시 가장 긴 거리 제거
	>> 두 묶음이었던 센서 중 하나가 쪼개지면서 총 세 개의 묶음이 됨
	>> 세 개의 집중국
이런 식으로 k개의 집중국이 될 때까지 최대 거리를 제거
남은 거리들의 합 계산
'''
sensor = sorted(sensor)
dist = sorted([sensor[i + 1] - sensor[i] for i in range(n - 1)])
# output
print(sum(dist[: (n - 1) - (k - 1)]))