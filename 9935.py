### 시간 초과 ###
import re
# input
s = input()
bomb = input()
cnt = 1
# process
while cnt != 0:
	s, cnt = re.subn(bomb, '', s)
# output
print(s) if s != "" else print("FRULA")