def add_numbers(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b


def get_greeting(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(get_greeting("GitHub Actions"))
    print(f"2 + 3 = {add_numbers(2, 3)}")
