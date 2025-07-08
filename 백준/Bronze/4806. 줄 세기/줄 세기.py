import sys

# 변경: main 제거 후 즉시 실행
count = sum(1 for _ in sys.stdin)  # sys.stdin의 각 줄을 1씩 세어 합산
print(count)