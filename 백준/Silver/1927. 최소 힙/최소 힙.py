import sys
input = sys.stdin.readline

heap =[float("inf")]

def insert(x):
    heap.append(x)
    i = len(heap) - 1

    while( i > 1 and heap[i // 2] > x):
        heap[i] = heap[i//2]
        i //= 2
        heap[i] = x

def pop():
    if len(heap) == 1 : return 0
    if len(heap) == 2 : return heap.pop()
    root= heap[1]
    # 마지막 원소를 루트로 이동
    heap[1] = heap.pop()
    i = 1
    cur = heap[1]

    #자식이 존재하는동안 반복
    while i * 2 < len(heap):
        left = i * 2  # 왼쪽 자식 인덱스
        right = i * 2 + 1  # 오른쪽 자식 인덱스
        
        # '오른쪽 자식이 존재'하고 '오른쪽 자식이 왼쪽 자식보다 더 작으면' 오른쪽 자식을 선택
        if right < len(heap) and heap[left] > heap[right]:
            #오른쪽 자식 노드와 부모 노드를 교환
            child = heap[right]
            child_idx = right
        else :
            
            child = heap[left]
            child_idx = left
        # 현재 노드가 더 작으면 교환할 필요 없음
        if cur <= child: break

        heap[i] = child
        i = child_idx

    heap[i] = cur
    
    return root


for i in range(int(input())):

    x = int(input())
    if x == 0:
        #힙에서 가장 작은 값을 출력하고 그 값을 배열에서 제거
        print(pop())
    else:
        # x 값을 힙에 삽입
        insert(x)
