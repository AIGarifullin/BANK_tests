"""Test 3."""


def min_number_of_stairs_passage(n_t_data: list[int], stairs_data: list[int],
                                 value: int) -> int:
    """Минимальное количество проходов лестницы."""
    t = n_t_data[1]
    st_num_begin = stairs_data[0]
    st_num_person = stairs_data[value-1]
    st_num_end = stairs_data[-1]
    if st_num_person - st_num_begin <= t:
        res = st_num_end - st_num_begin
    elif (st_num_person - st_num_begin > t and
          (st_num_person - st_num_begin < st_num_end - st_num_person)):
        res = 2*(st_num_person - st_num_begin) + st_num_end - st_num_person
    elif (st_num_person - st_num_begin > t and
          (st_num_person - st_num_begin > st_num_end - st_num_person)):
        res = 2*(st_num_end - st_num_person) + st_num_person - st_num_begin
    return res


if __name__ == '__main__':
    n_t_params: list[int] = [int(num) for num in input().split()]
    stairs_nums: list[int] = [int(num) for num in input().split()]
    person_num: int = int(input())
    print(min_number_of_stairs_passage(n_t_params, stairs_nums, person_num))
