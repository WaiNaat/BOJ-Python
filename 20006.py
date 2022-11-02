'''
배열을 이용해서 각 방의 정보를 저장한다.
1. 해당 방의 레벨 제한
2. 해당 방의 현재 인원들
'''
import sys
input = sys.stdin.readline

# input & process
p, m = map(int, input().split())
room_level = []
room_players = []

for _ in range(p):
	level, id = input().split()
	level = int(level)

	room_found = False
	for room in range(len(room_level)):
		if room_level[room] - 10 <= level <= room_level[room] + 10 and len(room_players[room]) < m:
			room_players[room].append((level, id))
			room_found = True
			break
	
	if not room_found:
		room_level.append(level)
		room_players.append([(level, id)])	

for players in room_players:
	players.sort(key = lambda x: x[1])

# output
output = []
for i in range(len(room_players)):
	if len(room_players[i]) < m:
		output.append('Waiting!')
	else:
		output.append('Started!')

	for level, id in room_players[i]:
		output.append(f'{level} {id}')
print('\n'.join(output))