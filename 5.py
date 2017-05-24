"""
1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

-> 최소공배수
"""


def is_prime(num):
    if num == 2 or num == 3:
        return True

    if num % 2 == 0:
        return False

    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def solution(target_range):
    primes = []
    for i in target_range:
        if i == 0 or i == 1:
            continue
        if is_prime(i):
            primes.append(i)

    prime_count = {}
    for prime in primes:
        i = 1
        while prime ** i < target_range[-1]:
            i += 1

        prime_count[prime] = i - 1
    print(prime_count)

    result = 1
    for key, value in prime_count.items():
        result *= key ** value

    return result

if __name__ == '__main__':
    print(solution(range(1, 21)))
