"""
10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.

1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?
"""


def solution(number, target_numbers):
    multiples = []
    for target_number in target_numbers:
        for i in range(number):
            if i % target_number == 0:
                multiples.append(i)

    multiples_without_duplicate = set(multiples)
    return sum(multiples_without_duplicate)

if __name__ == '__main__':
    number = 1000
    target_numbers = [3, 5]
    print(solution(number, target_numbers))