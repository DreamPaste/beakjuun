import sys

# 분할 정복을 통해 
def searchRect(histogram, start, end):
    if start == end:
        return histogram[start]
    # 경계선
    
    mid = (start + end ) //2
    
    # 왼쪽과 오른쪽 직사각형
    leftRect = searchRect(histogram, start, mid)
    rightRect = searchRect(histogram, mid + 1, end)
    # 중앙을 포함하는 직사각형
    centerRect = searchMaxArea(histogram, start, mid, end)
    
    return max(leftRect, rightRect, centerRect)


def searchMaxArea(histogram, start, mid, end):
    
    height = histogram[mid]
    area = height
    left = mid
    right = mid

    while left > start or right < end:
        # 오른쪽으로 확장하며 넓이 계산
        if right < end :
            #1 left가 더 왼쪽으로 확장이 불가능한 경우
            #2 왼쪽으로 확장했을때 새로 포함될 막대보다 오른쪽으로 확장했을떄 새로 포함될 막대가 큰 경우(유리한 쪽)
            if left == start or histogram[left - 1] < histogram[right + 1]:
            
                right +=1
                height = min(height, histogram[right])
            #왼쪽으로 확장한다.
            else :
                left -=1
                height = min(height, histogram[left])
        # 오른쪽 확장이 불가능하므로 왼쪽 확장
        else :
            left -=1
            height = min(height, histogram[left])
        
        # 넓이 계산(높이 * 확장한 너비)
        area = max(area, height * (right - left + 1)) 
   
    return area

while True:
    # 한 줄을 입력받고 숫자로 변환
    line = list(map(int, sys.stdin.readline().split()))
    
    # 입력값이 [0]이면 종료
    if line == [0]:
        break
    
    # n과 histogram 배열 분리
    n = line[0]
    histogram = line[1:]
    print(searchRect(histogram, 0, n-1))

