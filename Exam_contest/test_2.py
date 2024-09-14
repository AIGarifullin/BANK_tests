"""Test 2."""


def conclusion(value: int, data: list[int]) -> str:
    """Восстановление иформации с журнала."""
    for page in data:
        if page == -1:
            data.remove(-1)
    if data == sorted(data):
        result = 'YES\n' + ' '.join([str(num) for num in range(1, value + 1)])
    else:
        result = 'NO'
    return result


if __name__ == '__main__':
    number_of_day: int = int(input()) 
    page_numbers: list[int] = [int(num) for num in input().split()]
    print(conclusion(number_of_day, page_numbers))
