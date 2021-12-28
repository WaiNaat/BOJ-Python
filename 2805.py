# function
def cut(value):
	'''
	톱날을 땅에서 value미터만큼 올렸을 때 잘리는 양
	'''
	timber = 0
	for tree in trees:
		result = tree - value
		if result > 0: timber += result
	return timber

# input
treeNum, goal = map(int, input().split())
trees = list(map(int, input().split()))
# process
'''
톱날을 x미터만큼으로 해서 자를 때
자른 결과 < 목표치 면 톱날을 낮춘다.
아니면 톱날을 높인다.
'''
left = 0
right = max(trees) + 1
while left < right:
	mid = (left + right) // 2
	if cut(mid) < goal: right = mid
	else: left = mid + 1
# output
print(left - 1)

'''
right = max(trees) + 1?
>> 답이 max(trees)일 경우 right=max(trees)로 출발하면
	mid = max(trees)가 절대 될 수 없음.
	왜? left+1=right인 경우에 mid는 항상 left이기 때문에
	다음 iteration에서 mid=max(trees)를 검사 못하고 무조건 탈출함.
	반면에 right=max(trees)+1로 하면 같은 이유로
	mid = max(trees)는 검사하지만 mid=max(trees)는 검사할 수도 없고 해서도 안 됨.

print(left - 1)
이 함수는 bisect모듈의 bisect_right와 원리가 같음.
bisect_right는 정렬되어 있는 배열에서 새로 들어오는 값 x가 들어갈 index를 찾아줌.
(만약 중복되는 값이 있으면 그들 중 가장 오른쪽 값의 다음 index)
하지만 지금은 x를 배열에 넣으려고 하는 게 아니라 1을 빼줘야 함.
'''