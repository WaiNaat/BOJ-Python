# 0. 개요
[Baekjoon Online Judge](https://www.acmicpc.net/)에서 [제가 푼 문제들](https://www.acmicpc.net/user/twicedtna)의 코드를 저장하는 곳입니다. 틀린 코드도 있으며, 그 경우 코드 첫 부분에 틀렸다고 쓰여 있습니다. 같은 문제에 대해 여러 버전의 코드가 있을 수 있는데, 이 경우 보통 마지막 버전이 최종 버전입니다.

이 문서에는 제가 문제를 풀면서 염두에 두어야 할 것들을 따로 정리하고자 합니다. 제 편의를 위해 높임말을 쓸 수도 있고 쓰지 않을 수도 있으니 양해 부탁드립니다.

* * *
# 1. 알고리즘과 관련은 없지만 염두에 두어야 할 것들
### 1.1. 정답 출력 양식 꼼꼼히 확인하기. 
<span style="color:red">**각 줄 맨 마지막에 공백이 허용되는지**</span>   
<span style="color:red">**출력 대소문자**</span>

### 1.2. 문제 꼼꼼히 읽기
시키는 대로 안 해놓고 왜 안 되냐고 변명ㄴ    
문제를 잘 읽어야 예외 상황 고려하기에도 편함.

### 1.3. 입력과 동시에 처리
계산에 있어서 점화식처럼 다음 입력값을 고려할 필요가 없을 때는 list에 미리 모든 입력을 다 저장한 후에 계산하는 것이 아니라 즉석에서 받으면서 처리하면 훨씬 효율적이다.
### 1.4. flag
두 subroutine을 번갈아서 하는 경우에는 flag를 사용하면 편하다.
### 1.5. 자주 참조되는 값은 새로운 변수에 할당
어떤 배열 형식 자료에서 같은 index의 값을 여러 번 사용하는 경우에는 새로운 변수를 만들어 값을 할당한 후 그 변수를 쓰는 것이 좋다.   
왜? 정확하진 않지만 개인적인 생각을 써 본다.
```Python
a = 1
arr[i] = 1
```
위쪽은 a에 1 객체의 포인터가 들어 있고, 아래쪽은 arr 기본 주소에서 i만큼의 위치에 1 객체의 포인터가 들어 있다. 파이썬에서는 모든 것들이 reference type이니까 "i만큼의 위치"라는 말에서 'i' 역시 값이 아니라 포인터일 가능성이 높다고 본다. 그러면 arr[i]의 올바른 위치를 찾는 데 상대적으로 더 많은 시간이 걸릴 것이라 생각한다.
### 1.6. 재귀와 스택
~~파이썬에서 재귀를 할 때, 나만의 스택을 만들어서 재귀를 대체할 수 있다면 그렇게 하는 것이 메모리 측면에서 효율적이다.~~ 확인 필요

### 1.7. itertools.chain
for문 같은 곳에서 범위가 난잡하면 itertools의 chain()을 통해 합칠 수 있다.
```Python
from itertools import chain
a = range(10)
b = [7,77,777]
for x in chain(a, b): print(x, end=' ')
'''
1 2 3 4 5 6 7 8 9 7 77 777
'''
```
### 1.8. itertools.combinations
```Python
from itertools import combinations
combinations(iterable, n)
```
iterable에서 n개를 뽑는 조합을 구합니다. for문을 통해 내용물을 하나씩 뽑을 수 있음.
### 1.9. bisect
```Python
from bisect import bisect_left, bisect_right
bisect_right(array, value, left=0, right=len(array))
```
bisect_right는 array가 정렬되어 있다는 가정 하에, value를 array에 순서를 망가뜨리지 않고 집어넣으려 할 때 어떤 index에 들어가야 할 지를 구해줍니다. right인 이유는 만약 value와 같은 값이 array에 있으면 그 값 바로 오른쪽에 넣을 수 있도록 해 주는 거라서. 자매품으로 bisect_left가 있음.    
이 함수의 코드는 [여기](https://github.com/python/cpython/blob/3.8/Lib/bisect.py)에서 직접 확인 가능.
### 1.10. string slicing
```Python
s = s[start : end : step]
```
step이 -1일 경우 문자열을 반전시킬 수 있습니다.
### 1.11 itertools.product
```Python
from itertools import product
product(iterable, repeat = n)
```
iterable에 대해 n중 for문을 돌리는 것과 같습니다.
* * *
# 2. 슬라이딩 윈도우
재밌는 기법. O(n) 시간이니 잘 생각해서 쓰자.

* * *
# 3. DFS/BFS

```Python
sys.setrecursionlimit() # 파이썬으로 재귀형 DFS 구현 시
```

둘 중에 하나로 해서 안 되면 오기 부리지 말고 다른 걸로 해 보기.   
(M, N)이 (가로, 세로)인지 (세로, 가로)인지 잘 보고 헷갈리지 않게 width, height로 바꿔서 쓰자.

* * *
# 4. Heap
삽입: O(log n)   
뿌리 제거: O(log n)

파이썬의 heapq 모듈은 최소 힙을 구현하기 때문에 최대 힙을 원하면 원소를 넣을 때 부호를 바꿔서 넣는 등의 추가 처리가 필요하다.

* * *
# 5. 그리디
그리디 문제의 핵심은 이 문제가 그리디 알고리즘으로 풀리는 문제임을 파악하는 것과 기준점을 찾는 것이다. 그리디 알고리즘의 증명법 세 가지 중 "Greedy Stays Ahead" 방법을 염두에 두고 어떤 값이 기준이 될 수 있는지 생각해야 한다. 이 기준점을 제대로 생각하지 못 하면 답을 볼 수밖에 없는 상황이 된다.

***
# 6. 이분탐색
**left와 right 범위 똑바로 생각하기.**   
순수 이분탐색이 아닌 경우 문제에 따라 bisect_left와 bisect_right 중 어떤 성격인지 생각하기.