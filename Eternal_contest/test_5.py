"""Test 5."""


def max_test_value(left_right_data: list[int]) -> int:
    """Максимальная количество тестов."""
    left, right = left_right_data[0], left_right_data[1]
    if (1 <= left <= 10**18 and 1 <= right <= 10**18):
        pass
    else:
        print('Error: Введите корректные значения l, r')
        return False

    num_list = list(range(1, 10))
    total_list = num_list[:]
    num = 1
    i = 0
    while num <= right:
        for k in num_list:
            num = 10*total_list[i] + k
            total_list.append(num)
            i += 1

    count = 0
    for num in total_list:
        if num in range(left, right + 1):
            count += 1
    return count


if __name__ == '__main__':
    left_right_params: list[int] = [int(num) for num in input().split()]
    print(max_test_value(left_right_params))
