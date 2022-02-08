import sys
input = sys.stdin.readline
# input
n = int(input())
grade = [tuple(map(int, input().split())) for _ in range(n)]
# process
'''
grade(i, left/right)를 각각 i번째 책상의 왼쪽, 오른쪽 학생의 성적,
opt(i, left/right)를 각각 i번째 ~ 학생을 포함하여 채점할 수 있는 최대 학생 수라 하면
opt(i, left) =
	opt(i-1, left) + 1  (grade(i-1, left)=grade(i, left))
	opt(i-1, right) + 1  (grade(i-1, right)=grade(i, left))
	1  (앞 줄 학생들과 본인의 성적이 다를 경우)
같은 방식으로 opt(i, right)도 구할 수 있음
'''
opt = [[1, 1] for _ in range(n)]
sol_cnt  = 1
sol_grade = min(grade[0])

for i in range(1, n):
	for k in (0, 1):
		if grade[i][k] == grade[i - 1][0]:
			opt[i][k] = opt[i - 1][0] + 1
		elif grade[i][k] == grade[i - 1][1]:
			opt[i][k] = opt[i - 1][1] + 1
	
		if opt[i][k] > sol_cnt or (opt[i][k] == sol_cnt and grade[i][k] < sol_grade):
			sol_cnt = opt[i][k]
			sol_grade = grade[i][k]
# output
print(f"{sol_cnt} {sol_grade}")