# input
n, k = map(int, input().split())
quests = list(map(int, input().split()))

# process
# 경손실 최소화하려면 경험치를 적게 주는 퀘스트부터 해야 한다.
quests.sort()
# 아케인스톤 1개의 경험치 
# = 모든 퀘스트 경험치의 합 - 활성화 이전까지 한 퀘스트의 경험치 합
expSum = sum(quests)
expLoss = 0
sol = 0
for i in range(k):
	expLoss += quests[i]
	sol += expSum - expLoss

# output
print(sol)