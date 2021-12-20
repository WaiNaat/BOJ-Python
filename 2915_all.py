# input
for x in ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']:
	for y in ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']:
		B = x + y
		print("%s\t\t" % B, end='')
# process
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