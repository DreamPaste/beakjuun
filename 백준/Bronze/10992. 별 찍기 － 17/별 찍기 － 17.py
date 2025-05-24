N = int(input().strip())

if N == 1:                  # (변경 ❶) N이 1이면 바로 종료
    print('*')
else:
    # 1) 꼭대기
    print(' ' * (N - 1) + '*')

    # 2) 중간 줄 (행 번호 i : 2 ~ N-1)
    for i in range(2, N):
        leading = ' ' * (N - i)        # 앞 공백
        inner   = ' ' * (2 * i - 3)    # 내부 공백
        print(f'{leading}*{inner}*')

    # 3) 바닥
    print('*' * (2 * N - 1))