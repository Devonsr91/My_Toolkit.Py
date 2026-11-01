
def calculate_average(numbers):
    """Return the average of a list of numbers, or 0 if empty."""
    if len(numbers) == 0:
        return 0

    total = 0
    for number in numbers:
        total += number

    return total / len(numbers)


def find_max_and_min(numbers):
    """Return a tuple containing the largest and smallest numbers."""
    if len(numbers) == 0:
        return (None, None)

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return (largest, smallest)


def count_occurrences(items, target):
    """Return how many times target appears in items."""
    count = 0

    for item in items:
        if item == target:
            count += 1

    return count


def is_palindrome(text):
    """Return True if text reads the same backward, ignoring case and spaces."""
    cleaned = "".join(text.lower().split())
    return cleaned == cleaned[::-1]


def create_report(title, scores):
    """Return a formatted report containing average, maximum, and minimum."""
    average = calculate_average(scores)
    largest, smallest = find_max_and_min(scores)

    report = f"Report: {title}\n"
    report += f"Average: {average}\n"

    if len(scores) == 0:
        report += "Max: N/A\n"
        report += "Min: N/A"
    else:
        report += f"Max: {largest}\n"
        report += f"Min: {smallest}"

    return report


if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]

    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))

    # Edge case tests
    print("\n--- Edge Case Tests ---")

    print(f"Empty average: {calculate_average([])}")
    print(f"Empty max/min: {find_max_and_min([])}")

    print(f"Count repeated 2s: {count_occurrences([2, 2, 3, 2], 2)}")
    print(f"Count missing 5: {count_occurrences([1, 2, 3], 5)}")

    print(f"Phrase palindrome: {is_palindrome('A man a plan a canal Panama')}")
    print(f"Single character: {is_palindrome('a')}")
    print(f"Mixed case: {is_palindrome('RaceCar')}")
    print(f"Empty text: {is_palindrome('')}")
    print(f"Not palindrome: {is_palindrome('hello')}")

    print()
    print(create_report("Empty Report", []))
