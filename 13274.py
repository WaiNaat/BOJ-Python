import sys

input = sys.stdin.readline

_, queryCount = map(int, input().split())
sequence = list(map(int, input().split()))

sequence.sort()

for _ in range(queryCount):
    left, right, value = map(int, input().split())

    if value == 0:
        continue

    next = []
    isLeftUneffectedByQuery = value > 0
    if isLeftUneffectedByQuery:
        queryPointer = left - 1
        effectedPointer = right
        next = sequence[0 : left - 1]

        while queryPointer < right and effectedPointer < len(sequence):
            if sequence[queryPointer] + value < sequence[effectedPointer]:
                next.append(sequence[queryPointer] + value)
                queryPointer += 1
            else:
                next.append(sequence[effectedPointer])
                effectedPointer += 1

        while queryPointer < right:
            next.append(sequence[queryPointer] + value)
            queryPointer += 1
        while effectedPointer < len(sequence):
            next.append(sequence[effectedPointer])
            effectedPointer += 1
    else:
        queryPointer = left - 1
        effectedPointer = 0

        while queryPointer < right and effectedPointer < left - 1:
            if sequence[queryPointer] + value < sequence[effectedPointer]:
                next.append(sequence[queryPointer] + value)
                queryPointer += 1
            else:
                next.append(sequence[effectedPointer])
                effectedPointer += 1

        while queryPointer < right:
            next.append(sequence[queryPointer] + value)
            queryPointer += 1
        while effectedPointer < left - 1:
            next.append(sequence[effectedPointer])
            effectedPointer += 1

        next.extend(sequence[right : len(sequence)])

    sequence = next

print(*sequence)
