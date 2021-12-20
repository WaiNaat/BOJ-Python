# input
B = input()
# process
'''
XI는 IX로 바꾼다.
LX는 XL로 바꾼다.
VI는 IV로 바꾼다.
'''
if B[ :2] == "LX" and B[ :3] != "LXX":
	B = B.replace("LX", "XL")

if B[len(B) - 2: ] == "XI":
	B = B.replace("XI", "IX")

if B[ :2] == "LX" and B[ :3] != "LXX":
	B = B.replace("LX", "XL")

units = None
for i in range(len(B)):
	if B[i] == 'V' or B[i] == 'I':
		units = i
		break
if units is not None:
	if B[units: ] == "VI":
		B = B.replace("VI", "IV")

# output
print(B)