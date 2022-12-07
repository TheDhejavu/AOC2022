import os
import bisect
import sys

def cal_calories_counting(values):
    max_ef_calories = 0
    current_ef_calories = 0
    efs_calories = []
    for value in values:
        if value == '':
            max_ef_calories = max(max_ef_calories, current_ef_calories)
            current_ef_calories = 0
            if max_ef_calories not in efs_calories:
                bisect.insort(efs_calories, max_ef_calories) 
            continue

        current_ef_calories += int(value)

    return efs_calories

def calorie_counting_part1(values):
    efs_calories = cal_calories_counting(values)
    return efs_calories[-1]


def calorie_counting_part2(values):
    efs_calories = cal_calories_counting(values)
    return sum(efs_calories[-3:])

dir = os.path.abspath(os.path.dirname(__file__))
if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path) as file:
            _input = file.read().splitlines()
            part1 = calorie_counting_part1(_input)
            part2 = calorie_counting_part2(_input)
            print('Part 1: ', part1)
            print('Part 2:', part2)

