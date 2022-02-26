from itertools import combinations

# function
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
person = set([i for i in range(n)])
sol = 1234
for team in combinations(range(n), n // 2):
	status_diff = abs(computeTeamStatus(team) - computeTeamStatus(person - set(team)))
	sol = min(sol, status_diff)

# output
print(sol)