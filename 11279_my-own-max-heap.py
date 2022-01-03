import sys
input = sys.stdin.readline
# class
class Heap:
	'''
	나만의 최대 힙.
	push, pop 연산 지원.
	최댓값은 peek 함수로 볼 수 있음.
	k번 인덱스에 대한 자식 노드 인덱스는 2k+1, 2k+2.
	'''
	def __init__(self):
		self.heap = []
	
	def push(self, value):
		'''
		새로운 노드를 맨 마지막에 넣는다.
		새로운 노드와 부모를 비교해서 새 노드가 더 크면 부모와 바꾼다.				
		'''
		self.heap.append(value)
		idx = len(self.heap)
		parent = idx >> 1
		while parent >= 1 and self.heap[parent - 1] < value:
			self.heap[idx - 1], self.heap[parent - 1] \
				= self.heap[parent - 1], self.heap[idx - 1]
			idx = parent
			parent = idx >> 1

	def pop(self):
		'''
		루트를 제거하고 맨 마지막 노드를 루트로 옮긴다.
		루트와 자식을 비교해서 루트가 더 작으면 자식과 바꾼다.
		자식이 둘일 경우 더 큰 자식과 바꾼다.
		'''
		if not self.heap: return 0
		ret = self.heap[0]
		self.heap[0] = self.heap[-1]
		self.heap.pop()
		idx = 1
		child = idx << 1
		while True:
			leftChild = None
			rightChild = None
			if child <= len(self.heap): leftChild = child
			if child + 1 <= len(self.heap): rightChild = child + 1

			if leftChild is not None and rightChild is None:
				if self.heap[idx - 1] < self.heap[leftChild - 1]:
					self.heap[idx - 1], self.heap[leftChild - 1] \
						= self.heap[leftChild - 1], self.heap[idx - 1]
					idx = leftChild
					child = idx << 1
				else: break
			elif rightChild is not None and leftChild is None:
				if self.heap[idx - 1] < self.heap[rightChild - 1]:
					self.heap[idx - 1], self.heap[rightChild - 1] \
						= self.heap[rightChild - 1], self.heap[idx - 1]
					idx = rightChild
					child = idx << 1
				else: break
			elif leftChild is not None and rightChild is not None:
				if self.heap[leftChild -1] > self.heap[rightChild - 1]:
					if self.heap[idx - 1] < self.heap[leftChild - 1]:
						self.heap[idx - 1], self.heap[leftChild - 1] \
						= self.heap[leftChild - 1], self.heap[idx - 1]
						idx = leftChild
						child = idx << 1
					else: break
				else:
					if self.heap[idx - 1] < self.heap[rightChild - 1]:
						self.heap[idx - 1], self.heap[rightChild - 1] \
						= self.heap[rightChild - 1], self.heap[idx - 1]
						idx = rightChild
						child = idx << 1
					else: break
			else: break
		return ret

# input
n = int(input())
h = Heap()
for _ in range(n):
	op = int(input())
# process & output
	if op == 0: 
		print(h.pop())
	else: h.push(op)