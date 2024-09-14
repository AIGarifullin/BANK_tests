"""Test 1."""


def cost_of_internet_traffic(data: list[int]) -> int:
    """Суммарные расходы Кости за интернет."""
    a: int = data[0]
    b: int = data[1]
    c: int = data[2]
    d: int = data[3]
    scope = range(1, 101)
    if (a and b and c and d) in scope:
        if d > b:
            res = a + (d - b)*c
        else:
            res = a
    return res


if __name__ == '__main__':
    parameters: list[int] = [int(num) for num in input().split()]
    print(cost_of_internet_traffic(parameters))
