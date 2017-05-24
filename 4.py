"""
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?
"""
from python_functions.decorator import time_it


def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

@time_it
def solution(digit_num):
    three_digits = range(10 ** (digit_num - 1), 10 ** digit_num)
    largetst_palindrome = 1
    for i in three_digits:
        for j in three_digits:
            if is_palindrome(i*j):
                if largetst_palindrome < i*j:
                    largetst_palindrome = i*j

    return largetst_palindrome


if __name__ == '__main__':
    print(solution(3))
