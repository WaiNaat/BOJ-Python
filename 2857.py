import re

found = False
for i in range(1, 6):
	if re.search("FBI", input()) is not None:
		print(i, end=' ')
		found = True
if not found: print("HE GOT AWAY!")