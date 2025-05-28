import sys
from math import pi

menu_number = 1
lines = sys.stdin.read().strip().split('\n')
idx = 0

while idx < len(lines):
    n = int(lines[idx])
    if n == 0:
        break

    idx += 1
    best_value = float('inf')
    best_diameter = 0

    for _ in range(n):
        d, p = map(int, lines[idx].split())
        area = pi * (d / 2) ** 2
        cost_per_sq_inch = p / area

        if cost_per_sq_inch < best_value:
            best_value = cost_per_sq_inch
            best_diameter = d
        idx += 1

    print(f"Menu {menu_number}: {best_diameter}")
    menu_number += 1
