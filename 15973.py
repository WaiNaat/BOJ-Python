### 틀렸습니다 ###

# function
def findVertex(x1, y1, x2, y2):
    return ((x1, y1), (x2, y2), (x1, y2), (x2, y1))

def isFace(box1, box2):
    '''
    box1의 두 개 이상의 변이 box2 내부를 지나가면 face
    '''
    cnt = 0
    # 위쪽 변이 내부를 지나는 경우
    if box2[1] <= box1[3] <= box2[3] \
        and box2[0] < box1[2] and box1[0] < box2[2]:
        cnt += 1
    # 오른쪽 변이 내부를 지나는 경우
    if box2[0] <= box1[2] <= box2[2] \
        and box1[1] < box2[3] and box2[1] < box1[3]:
        cnt += 1
    # 아래쪽 변이 내부를 지나는 경우
    if box2[1] <= box1[1] <= box2[3] \
        and box2[0] < box1[2] and box1[0] < box2[2]:
        cnt += 1
    # 왼쪽 변이 내부를 지나는 경우
    if box2[0] <= box1[0] <= box2[2] \
        and box1[1] < box2[3] and box2[1] < box1[3]:
        cnt += 1
    return True if cnt >= 2 else False

def isLine(box1, box2):
    """box1의 어떤 쪽 변에서 box2와 만나는 경우"""
    # 위쪽 변에서 만나는 경우
    if box1[3] == box2[1] \
        and (box1[0] <= box2[0] < box1[2] or box1[0] < box2[2] <= box1[2]):
        return True
    # 오른쪽 변에서 만나는 경우
    elif box1[2] == box2[0] \
        and (box1[1] <= box2[1] < box1[3] or box1[1] < box2[3] <= box1[3]):
        return True
    # 아래쪽 변에서 만나는 경우
    elif box1[1] == box2[3] \
        and (box1[0] <= box2[0] < box1[2] or box1[0] < box2[2] <= box1[2]):
        return True
    # 왼쪽 변에서 만나는 경우
    elif box1[0] == box2[2] \
        and (box1[1] <= box2[1] < box1[3] or box1[1] < box2[3] <= box1[3]):
        return True
    
    return False

def isPoint(box1, box2):
    # 네 점을 먼저 구함
    box1 = findVertex(*box1)
    box2 = findVertex(*box2)
    # 같은 점이 있으면 point
    for v in box1:
        if v in box2:
            return True
    return False

# input
box1 = tuple(map(int, input().split()))
box2 = tuple(map(int, input().split()))

# process
if isFace(box1, box2) or isFace(box2, box1):
    sol = "FACE"
elif isLine(box1, box2) or isLine(box2, box1):
    sol = "LINE"
elif isPoint(box1, box2):
    sol = "POINT"
else:
    sol = "NULL"

# output
print(sol)