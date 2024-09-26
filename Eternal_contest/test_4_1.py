"""Test 4."""


def max_diff_between_begin_and_end_sums(n_k_data: list[int],
                                        a_data: list[int]) -> int:
    """Максимальная разность между начальной и конечной суммой."""
    n, k = n_k_data[0], n_k_data[1]
    a_data = sorted(a_data)
    res = 0
    i = 0
    while i < k and k <= n:
        if a_data[-1] < 10:
            res += 9 - a_data[i]
        elif 10 <= a_data[-1] < 99:
            res += 90 + a_data[-1-i] % 10 - a_data[-1-i]
        else:
            res += 90 + a_data[-2-i] % 10 - a_data[-2-i]
        i += 1
    return res


if __name__ == '__main__':
    n_k_params: list[int] = [int(num) for num in input().split()]
    a_nums: list[int] = [int(num) for num in input().split()]
    print(max_diff_between_begin_and_end_sums(n_k_params, a_nums))
