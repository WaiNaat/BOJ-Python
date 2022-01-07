s = input()
while len(s) > 4:
	s = s.replace("PPAP", "P")
if s == "PPAP":
	print("PPAP")
else: 
	print("NP")