'''
선로의 높이는 높음/낮음 단 두개임

즉 높이가
시작점 < 끝점: 마지막에 무조건 오르막길이 하나 있어야함
시작점 = 끝점: 오르막개수=내리막개수여야함
시작점 > 끝점: 마지막에 무조건 내리막길이 하나 있어야함

두 번의 질문으로 해결가능
'''
import sys
input = sys.stdin.readline

N = int(input())

print('? 1')
sys.stdout.flush()
start = int(input())

print(f'? {N}')
sys.stdout.flush()
end = int(input())

print(f'! {end - start}')
sys.stdout.flush()