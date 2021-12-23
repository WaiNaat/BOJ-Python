import sys
input = sys.stdin.readline
# input
height, width = map(int, input().split())
board = [input().rstrip() for _ in range(height)]
# process
'''
max(M)=max(N)=50이므로 체스판의 크기를 k라 할 때
O(kMN) 완전탐색 알고리즘 사용 가능.

8*8 체스판을 일종의 필터처럼 생각,
보드의 좌상단부터 한칸씩 체스판을 이동시키면서 개수 게산.
'''
# 체스판 제작
wline = "WBWBWBWB"
bline = "BWBWBWBW"
chessW = [wline, bline] * 4
chessB = [bline, wline] * 4
# 체스판 필터 이동
sol = 64
for h in range(height - 7):
	for w in range(width - 7):
		# 다시 칠해야 하는 개수 세기
		cntB = 0
		cntW = 0
		for i in range(8):
			for j in range(8):
				cur = board[h + i][w + j]
				if chessW[i][j] != cur:
					cntW += 1
				if chessB[i][j] != cur:
					cntB += 1
		sol = min(sol, cntB, cntW)
# output
print(sol)