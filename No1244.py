import sys
input = sys.stdin.readline

switchN = int(input())
switch = list(map(int, input().split()))
studentN = int(input())
for _ in range(studentN):
	sex, num = list(map(int, input().split()))
	if sex == 1:
		for i in range(switchN):
			if (i+1) % num == 0:
				switch[i] = 0 if switch[i]==1 else 1
	else:
		i = 1
		switch[num-1] = 0 if switch[num-1]==1 else 1
		while num-1+i < switchN and num-1-i >= 0:
			if switch[num-1-i] == switch[num-1+i]:
				switch[num-1-i] = switch[num-1+i] = 0 if switch[num-1-i]==1 else 1
				i += 1
			else:
				break

for i in range(switchN):
	sys.stdout.write("%d " % switch[i])
	if (i+1) % 20 == 0: sys.stdout.write("\n")