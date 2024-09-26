"""Test 3."""


def min_number_of_stairs_passage(n_t_data: list[int], stairs_data: list[int],
                                 value: int) -> int:
    """Минимальное количество проходов лестницы."""
    t = n_t_data[1]
    min_stairs = stairs_data[0]
    x = stairs_data[value-1]
    max_stairs = stairs_data[-1]
    if x - min_stairs <= t:
        res = max_stairs - min_stairs
    else:
        way_1 = 2*(x - min_stairs) + max_stairs - x
        way_2 = 2*(max_stairs - x) + x - min_stairs
        res = min(way_1, way_2)
    return res


if __name__ == '__main__':
    n_t_params: list[int] = [int(num) for num in input().split()]
    stairs_nums: list[int] = [int(num) for num in input().split()]
    person_num: int = int(input())
    print(min_number_of_stairs_passage(n_t_params, stairs_nums, person_num))
