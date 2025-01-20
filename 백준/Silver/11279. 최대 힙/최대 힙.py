import sys
input = sys.stdin.readline
# 쉬운 구현을 위해 0번째 인덱스는 사용하지 않음
heap =[0]
def push(x):

    #1 우선 배열의 마지막에 값 삽입
    heap.append(x)
    i = len(heap) - 1
    #2 x값과 힙의 부모 노드 비교
    while i > 1 and x > heap[i//2]:
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
        # 오른쪽 자식이 존재하고 오른쪽 자식이 더 크다면
        
        if right < len(heap) and heap[left] < heap[right]:
            #오른쪽 자식 노드와 부모 노드를 교환
            child = heap[right]
            child_idx = right
        else :
            #왼쪽 자식이 더 크다면 왼쪽 자식과 부모 노드를 교환
            child = heap[left]
            child_idx = left

        if cur >= child: break

        heap[i] = child
        i = child_idx

    heap[i] = cur
    
    return root


for i in range(int(input())):
    x = int(input())

    if x == 0 :
        #배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거
        sys.stdout.write(str(pop()) + "\n")
    else :
        push(x)
        
   

