def calculate_team_difference(n, data):
    min_difference = float('inf')
    startTeam = [False] * n

    def backtracking(index, count):
        nonlocal min_difference

        if count == n // 2:
            start_strength = 0
            link_strength = 0

            for i in range(n):
                for j in range(n):
                    if startTeam[i] and startTeam[j]:
                        start_strength += data[i][j]
                    elif not startTeam[i] and not startTeam[j]:
                        link_strength += data[i][j]

            difference = abs(start_strength - link_strength)
            min_difference = min(min_difference, difference)
            return

        for i in range(index, n):
            if not startTeam[i]:
                startTeam[i] = True
                backtracking(i + 1, count + 1)
                startTeam[i] = False

    backtracking(0, 0)
    return min_difference

# 입력 처리
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
result = calculate_team_difference(n, data)
print(result)
