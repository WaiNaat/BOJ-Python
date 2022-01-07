import sys
input = sys.stdin.readline

# input & process
start, end, stEnd = list(map(int, input().replace(':', '').split()))

valid = set([])
sol = 0
chat = input()
while chat != "":
	time, id = chat.split()
	time = int(time[:2]) * 100 + int(time[3:])
	if time <= start:
		valid.add(id)
	elif end <= time <= stEnd and id in valid:
		valid.discard(id)
		sol += 1
	chat = input()

# output
print(sol)