#소트인사이드
num = list(input()) #입력(str)을 리스트로 변환
num = sorted(num,reverse=True) #내림차순 sort
print(''.join(map(str,num))) #join(map())을 사용하여 문자열로 변환