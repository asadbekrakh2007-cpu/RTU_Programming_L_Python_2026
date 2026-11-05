"""
Lab 2.2 - Comprehensions and Transformations
"""

NUMBERS = [3, 8, -2, 7, 0, -5, 10]


def squares(numbers: list[int]) -> list[int]:
    """Return a list with the square of each number (list comprehension)."""
    return [n ** 2 for n in numbers]


def positives(numbers: list[int]) -> list[int]:
    """Return only the numbers greater than 0 (list comprehension)."""
    # n > 0 (not >= 0), because 0 is NOT positive
    return [n for n in numbers if n > 0]


def even_squares(numbers: list[int]) -> set[int]:
    """Return a set of the squares of the even numbers (set comprehension)."""
    # n % 2 == 0 is also True for 0 and negative even numbers like -2
    return {n ** 2 for n in numbers if n % 2 == 0}


def cubes(numbers: list[int]) -> dict[int, int]:
    """Return a dict mapping each number to its cube (dict comprehension)."""
    return {n: n ** 3 for n in numbers}


if __name__ == "__main__":
    # Keep all print() calls inside this block, otherwise the
    # autograder cannot import the file.
    print(f"Squares: {squares(NUMBERS)}")
    print(f"Positives: {positives(NUMBERS)}")
    print(f"Even squares: {even_squares(NUMBERS)}")
    print(f"Cubes: {cubes(NUMBERS)}")