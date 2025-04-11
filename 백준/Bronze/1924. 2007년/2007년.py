# 월별 일수 배열
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 요일 배열
week_days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

# 사용자로부터 월과 일을 입력받음
month, day = map(int, input().split())

# 총 일수 계산: 이전 달까지의 일수 합 + 현재 달의 일
total_days = sum(month_days[:month - 1]) + day

# 요일 결정: 총 일수를 7로 나눈 나머지를 인덱스로 사용
print(week_days[total_days % 7])
