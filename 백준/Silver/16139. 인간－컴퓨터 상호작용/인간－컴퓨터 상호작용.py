#인간 컴퓨터 상호작용
# 문자열 S에서, 특정 알파벳 a와, 구간[l,r]이 주워지면,
#  해당 구간에 a가 얼마만큼 나타나는지 구함


## TEST CASE
'''
seungjaehwang
4
a 0 5
a 0 6
a 6 10
a 7 10
'''

S = input()
q = int(input())
result =[]
prefix_sum = {}
for char in set(S):
    prefix_sum[char] = [0] * len(S)

#누적합 계산
#리스트가 초기화된 상태에서, 마지막 요소는 항상 0이므로 i=0일때부터 순회 가능
for i in range(len(S)):
    for char in prefix_sum.keys():
        if char == S[i]:
            prefix_sum[char][i] = prefix_sum[char][i-1] + 1
            
        else :
            prefix_sum[char][i] = prefix_sum[char][i-1]


for i in range(q):
    a, l, r = input().split()
    #문자가 존재하지 않을 경우
    if a not in prefix_sum:
        result.append(0)
        
    #l값이 0 일 경우 분리
    elif int(l) == 0:
        result.append(prefix_sum[a][int(r)])
        
    else:
        result.append(prefix_sum[a][int(r)] - prefix_sum[a][int(l) - 1])

print("\n".join(map(str, result)))