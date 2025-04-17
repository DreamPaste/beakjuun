import sys

def reverse_words(line: str) -> str:
    return ' '.join(word[::-1] for word in line.split())
data = sys.stdin.read().splitlines()
T = int(data[0])  # 테스트 케이스 수
for i in range(1, T + 1):
        # 각 문장을 뒤집어서 출력
        print(reverse_words(data[i]))