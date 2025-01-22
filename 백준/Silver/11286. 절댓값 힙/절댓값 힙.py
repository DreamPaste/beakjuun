import sys
input = sys.stdin.readline
heap = [float('inf')]
def insert(x):
    heap.append(x)
    i = len(heap) -1
    # i가 루트 노드가 아니고, 
    # 부모가 절댓값 기준으로 더 크거나, 
    # 절댓값이 같을 경우 부모 값이 더 크다면 swap
    while i > 1 and ( abs(heap[i//2]) > abs(x) or 
                        (abs(heap[i//2]) == abs(x) and heap[i//2] > x) ): 
        #부모 노드와 자식 노드 swap
        heap[i] = heap[i//2]
        i//=2
        heap[i] = x

def popItem():
    if len(heap) == 1: return 0
    if len(heap) == 2: return heap.pop()


    root = heap[1]
    #마지막 원소를 루트 원소로 변경
    heap[1] = heap.pop()
    i = 1
    #마지막 원소(제일 큰 값)
    last_child = heap[1]

    #자식 노드를 탐색하는 동안 반복
    while i * 2 < len(heap): 
        L = i * 2
        R =i * 2 + 1
        # 두 자식의 절댓값, 실제 값 을 비교하여 더 작은 자식 선택
        #1 오른쪽 자식이 존재하고 왼쪽 자식보다 작다면
        #2 두 자식의 절대값이 동일하고 왼쪽 자식의 값이 더 크다면(양수)
        if R < len(heap) and (abs(heap[L]) > abs(heap[R])
                                or (abs(heap[L]) == abs(heap[R]) and heap[L] > heap[R])):
             
            child_idx = R
        else:
            child_idx = L
        child = heap[child_idx]
        # 마지막 원소(last_child)가 자식보다 우선순위가 높다면 종료
        # heap[i]와 child를 swap하지 않아도 된다.
        if abs(child) > abs(last_child) or (
            abs(child) == abs(last_child) and child >= last_child): 
            break

        heap[i] = child
        
        i = child_idx
    
    heap[i] = last_child
    return root



for _ in range(int(input())):
    x = int(input())
    if x == 0:
        print(popItem())
    else:
        insert(x)
    