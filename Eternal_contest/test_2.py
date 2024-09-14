"""Test 2."""


def min_number_of_cuts(value: int) -> int:
    """Минимальное количество разрезов рулета."""
    if value >= 1:
        cuts = 0
        while value > 1:
            cuts += 1
            value = (value + 1) // 2
    return cuts


if __name__ == '__main__':
    n: int = int(input())
    print(min_number_of_cuts(n))
