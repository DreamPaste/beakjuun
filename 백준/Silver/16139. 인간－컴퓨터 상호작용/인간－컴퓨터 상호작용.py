#인간 컴퓨터 상호작용
# 문자열 S에서, 특정 알파벳 a와, 구간[l,r]이 주워지면,
#  해당 구간에 a가 얼마만큼 나타나는지 구함

import sys

data = sys.stdin.readlines()

S = data[0].strip()  # 첫 번째 줄: 문자열 S
q = int(data[1].strip())  # 두 번째 줄: 쿼리 개수
queries = data[2:]  # 나머지 줄: 쿼리 데이터

#누적합 딕셔너리 생성
prefix_sum = {}
for char in set(S):
    prefix_sum[char] = [0] * (len(S)+1)


# 누적합 계산
for i in range(len(S)):
    for char in prefix_sum.keys():
        prefix_sum[char][i + 1] = prefix_sum[char][i]  # 이전 값 복사
    prefix_sum[S[i]][i + 1] += 1  # 현재 문자의 누적값 증가

result =[]
for query in queries:
    char, l, r = query.split()
    l, r = int(l), int(r)
    #문자가 존재할 경우
    if char in prefix_sum:
        result.append(prefix_sum[char][r + 1] - prefix_sum[char][l])
        
    #문자가 존재하지 않는 경우
    else:
        result.append(0)


        

# 정수를 문자열로 변환하여 출력
print('\n'.join(map(str, result)))