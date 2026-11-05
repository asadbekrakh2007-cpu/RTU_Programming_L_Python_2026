"""
Lab 2.3 - Operator Frequency Counter
"""

OPERATORS = ['+', '-', '*', '/', '(', ')']


def count_operators(expression: str) -> dict[str, int]:
    """Return a dict with the count of each operator in expression."""
    # Start with all six operators set to 0, in the required order
    counts = {op: 0 for op in OPERATORS}
    # Check every character; ignore digits, spaces and letters
    for char in expression:
        if char in counts:
            counts[char] += 1
    return counts


if __name__ == "__main__":
    # Keep all input() and print() calls inside this block, otherwise the
    # autograder cannot import the file.
    expression = input("Enter an arithmetic expression: ")
    print(f"Operator counts: {count_operators(expression)}")