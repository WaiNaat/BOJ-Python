# input
N = int(input())
lectures = [0 for _ in range(1000001)]
for lecture in map(int, input().split()):
	lectures[lecture] += 1
wishlist = list(map(int, input().split()))

# process
# 학생들이 매물 목록에서 원하는 강의를 하나씩 빼 간다.
# 빼 갈 수 없으면 그 학생은 원하는 걸 들을 수 없다.
stuNo = N
for i in range(N):
	wish = wishlist[i]
	if lectures[wish] > 0:
		lectures[wish] -= 1
		stuNo -= 1		

# output
print(stuNo)