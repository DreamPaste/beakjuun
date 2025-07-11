commands = [int(input()) for _ in range(10)]

# 시계 방향으로 나열된 방향들
directions = ['N', 'E', 'S', 'W']
current = 0  # 북쪽에서 시작

# 명령어에 따라 방향 이동 값
rotation = {1: 1, 2: 2, 3: -1}

# 각 명령에 대해 방향 누적
for cmd in commands:
    current = (current + rotation[cmd]) % 4

# 결과 출력
print(directions[current])
