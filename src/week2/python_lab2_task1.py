"""
Lab 2.1 - Simple Datasets and Aggregates
"""


def average(values: list[float]) -> float:
    """Return the average of values, or 0.0 for an empty list."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def largest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the largest population."""
    if not populations:
        return ("", 0)
    # max() returns the key with the largest value; on a tie it returns the first one
    city = max(populations, key=populations.get)
    return (city, populations[city])


def smallest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the smallest population."""
    if not populations:
        return ("", 0)
    # min() also returns the first key on a tie
    city = min(populations, key=populations.get)
    return (city, populations[city])


def total_population(populations: dict[str, int]) -> int:
    """Return the sum of all populations."""
    # sum() of an empty collection is 0, so no special case is needed
    return sum(populations.values())


if __name__ == "__main__":
    # Keep all print() calls inside this block, otherwise the
    # autograder cannot import the file.
    temperatures = [3, 5, 2, 4, 6, 7, 3]
    city_population = {
        "Riga": 605000,
        "Daugavpils": 78000,
        "Liepaja": 67000,
        "Jelgava": 55000,
        "Valmiera": 23000,
    }

    print(f"Average temperature: {average(temperatures):.1f}")

    name, pop = largest_city(city_population)
    print(f"Largest city: {name} - {pop}")

    name, pop = smallest_city(city_population)
    print(f"Smallest city: {name} - {pop}")

    print(f"Total population: {total_population(city_population)}")