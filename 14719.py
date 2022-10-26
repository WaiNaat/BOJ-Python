'''
높이 낮은데부터 올라가면서 한 층씩 물이 고이는 부분을 확인
어떤 구역이 막힘 뚫~림 막힘 이러면 물이 고이고 양쪽 중 하나라도 뚫려있으면 안고임
즉 막혔음을 확인했을 때 이전에 막힌적이 있다면 고임
'''
import sys
input = sys.stdin.readline

# input
H, W = map(int, input().split())
block_heights = tuple(map(int, input().split()))

# process
sol = 0
for h in range(1, H + 1):

    is_closed = False
    tmp = 0

    for block in block_heights:
        
        # 막혔을 경우
        if block - h >= 0:
            if is_closed:
                sol += tmp
            is_closed = True
            tmp = 0
        # 뚫렸을 경우
        else:
            tmp += 1

# output
print(sol)