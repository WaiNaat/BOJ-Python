# input
_ = input()
prob = input()
# process
'''
문제를 칠하는 방법
1. 전부 파란색으로 칠한 뒤 빨간 덩어리들만 빨간색으로 칠한다.
	>> 1 + (빨간 덩어리 수)
2. 전부 빨간색으로~
	>> 1 + (파란 덩어리 수)
blue/red_chunk := 빨간/파란 덩어리 수
isBlue := 이전까지 파란 덩어리를 세고 있었으면 True
'''
blue_chunk = red_chunk = 0
isBlue = False if prob[0] == 'B' else True
for p in prob:
	# 이전까지 세던 덩어리 색과 다른 색이 나오면 새로운 덩어리임.
	if p == 'B' and not isBlue:
		blue_chunk += 1
		isBlue = True
	elif p == 'R' and isBlue:
		red_chunk += 1
		isBlue = False
# output
print(1 + min(blue_chunk, red_chunk))