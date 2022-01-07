N = int(input())

inside = N-2 		# X 테두리 안쪽 빈칸
updown = 2 * N -3 	# X 위아래 빈칸
side = 0 			# X 좌우 빈칸

top = []
for _ in range(N): top.append('*')
for _ in range(updown): top.append(' ')
for _ in range(N): top.append('*')
top = ''.join(top)
print(top)

for _ in range(N-2):
	line = []
	side += 1
	updown -= 2
	for _ in range(side): line.append(' ')
	line.append('*')
	for _ in range(inside): line.append(' ')
	line.append('*')
	for _ in range(updown): line.append(' ')
	line.append('*')
	for _ in range(inside): line.append(' ')
	line.append('*')
	line = ''.join(line)
	print(line)

line = []
side += 1
updown -= 2
for _ in range(side): line.append(' ')
line.append('*')
for _ in range(inside): line.append(' ')
line.append('*')
for _ in range(inside): line.append(' ')
line.append('*')
line = ''.join(line)
print(line)

for _ in range(N-2):
	line = []
	side -= 1
	updown += 2
	for _ in range(side): line.append(' ')
	line.append('*')
	for _ in range(inside): line.append(' ')
	line.append('*')
	for _ in range(updown): line.append(' ')
	line.append('*')
	for _ in range(inside): line.append(' ')
	line.append('*')
	line = ''.join(line)
	print(line)

print(top, end='')