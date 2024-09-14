"""Test 3."""


def password_recovery(line: list[str], template: list[str],
                      k: int) -> str:
    """Восстановление пароля по шаблону."""
    window = []
    window.extend(line[-k:])
    for index in range(1, len(line)-k+1):
        for item in template:
            if not item in window:
                window = [line[-k-index]] + window
                window.pop()
    return ''.join(window)


if __name__ == '__main__':
    pressed_buttons: list[str] = list(input())
    password_requirement: list[str] = list(input())
    password_length: int = int(input())
    print(password_recovery(pressed_buttons, password_requirement,
                            password_length))
