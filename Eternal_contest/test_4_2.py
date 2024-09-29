"""Test 4."""


def max_diff_between_begin_and_end_sums(n_k_data: list[int],
                                        a_data: list[int]) -> int:
    """Максимальная разность между начальной и конечной суммой."""
    n, k = n_k_data[0], n_k_data[1]
    a_data = sorted(a_data)
    num_min, num_max = a_data[0], a_data[-1]
    if (1 <= n <= 10**3 and 1 <= k <= 10**4 and
            1 <= num_min and num_max <= 10**9):
        pass
    else:
        print('Error: Введите корректные значения n, k, или a_data')
        return False

    def digit_count(num):
        count = 0
        while num > 0:
            num //= 10
            count += 1
        return count
    count_min = digit_count(num_min)
    count_max = digit_count(num_max)

    res = 0
    i = 0
    while i < k and k <= n:
        if count_min == count_max:
            factor = 10**(digit_count(a_data[i]) - 1)
            res += (9 - a_data[i]//factor)*factor
        elif (count_min < count_max and
              digit_count(a_data[-1 - i]) > digit_count(a_data[-2 - i]) > 1):
            factor = 10**(digit_count(a_data[-1 - i]) - 1)
            res += (9 - a_data[-1 - i]//factor)*factor
        elif (count_min < count_max and
              (digit_count(a_data[-1 - i]) == digit_count(a_data[-2 - i]) or
               digit_count(a_data[-2 - i]) == 1)):
            factor = 10**(digit_count(a_data[-2 - i]) - 1)
            res += (9 - a_data[-2 - i]//factor)*factor
        i += 1
    return res


if __name__ == '__main__':
    n_k_params: list[int] = [int(num) for num in input().split()]
    a_nums: list[int] = [int(num) for num in input().split()]
    print(max_diff_between_begin_and_end_sums(n_k_params, a_nums))
