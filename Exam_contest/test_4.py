"""Test 4."""


def prime_number(num: int) -> bool:
    """Проверка простого числа."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def count_divisors(n: int) -> int:
    """Подсчет количества делителей числа n."""
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count


def count_composite_with_prime_divisors(num_l: int, num_r: int) -> int:
    """Подсчет количества составных чисел c количеством простых делителей."""
    composite_count = 0
    for num in range(num_l, num_r + 1):
        if num > 1:
            divisors = count_divisors(num)
            if divisors > 2 and not prime_number(num):
                if prime_number(divisors):
                    composite_count += 1

    return composite_count


if __name__ == '__main__':
    left_index: int = int(input())
    right_index: int = int(input())
    print(count_composite_with_prime_divisors(left_index, right_index))
