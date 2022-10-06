'''
기준: 같은 멈춤 횟수일때 가장 연료가 많이 남는 경우 선택

1. 현재 남은 연료로 갈 수 있는 거리 내의 주유소 중
   가장 연료를 많이 채울 수 있는 주유소 확인
2. 해당 주유소까지 이동 후 연료 충전
'''
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# input
N = int(input())
oil_station = [tuple(map(int, input().split())) for _ in range(N)]
L, P = map(int, input().split())

# process
oil_station.sort()
oil_station_idx = 0
truck_pos = 0
truck_fuel = P
stop = 0
heap = []

while truck_pos + truck_fuel < L:
	
	while oil_station_idx < N and oil_station[oil_station_idx][0] - truck_pos <= truck_fuel:
		pos, fuel = oil_station[oil_station_idx]
		heappush(heap, (-fuel, pos))
		oil_station_idx += 1

	if not heap:
		stop = -1
		break
	
	fuel, pos = heappop(heap)
	fuel = -fuel

	stop += 1
	truck_fuel -= pos - truck_pos
	truck_fuel += fuel
	truck_pos = pos

# output
print(stop)