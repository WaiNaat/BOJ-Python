# functions
def dfs(n):
	global sol
	
	# 양 팀 인원수가 맞춰졌으면 능력치 차이를 계산.
	if len(teamB) == n // 2:
		statusA = computeTeamStatus(teamA - set(teamB))
		statusB = computeTeamStatus(teamB)
		sol = min(sol, abs(statusA - statusB))
	
	# 백트래킹을 이용해 B팀을 한명씩 뽑음.
	for person in range(n):
		if visited[person] == 0 and (len(teamB) == 0 or teamB[-1] < person):
			visited[person] = 1
			teamB.append(person)
			dfs(n)
			teamB.pop()
			visited[person] = 0


def computeTeamStatus(team):
	# 주어진 팀의 능력치를 계산.
	ret = 0
	for s1 in team:
		for s2 in team:
			ret += status[s1][s2]
	return ret


# input
n = int(input())
status = [tuple(map(int, input().split())) for _ in range(n)]

# process
'''
백트래킹으로 n명의 사람 중 n/2명을 뽑는 경우를 센다.
	>> n과 m 문제 응용인데 뽑는 선수를 비내림차순으로 정렬해서 중복 팀 제거
사람을 뽑았으면 점수 차 계산.
'''
visited = [0 for _ in range(n)]
teamA = set([i for i in range(n)])
teamB = []
sol = 1234567
dfs(n)

# output
print(sol)