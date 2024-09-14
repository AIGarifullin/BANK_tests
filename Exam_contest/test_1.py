"""Test 1."""


def sorted_numbers(data: list[str]) -> str:
    """Отсортированное множество чисел."""
    values = [item.split('-') if '-' in item else item for item in data]
    numbers_list: list[int] = []
    for scope in values:
        if isinstance(scope, list):
            numbers_list.extend(range(int(scope[0]), int(scope[1]) + 1))
        else:
            numbers_list.append(int(scope))
    return ' '.join([str(num) for num in numbers_list])


if __name__ == '__main__':
    numbers: list[str] = input().split(',')
    print(sorted_numbers(numbers))
