"""
피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?
"""


def get_pibonacci(first, second, num):
    result = [first, second]
    while result[-1] + result[-2] < num:
        result.append(result[-1] + result[-2])

    return result


def solution(first, second, num):
    pibonacci = get_pibonacci(first, second, num)
    result = 0

    for number in pibonacci:
        if number % 2 == 0:
            result += number

    return result

if __name__ == '__main__':
    first, second, num = 1, 2, 4000000
    print(solution(first, second, num))