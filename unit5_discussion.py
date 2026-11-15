"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

from time import perf_counter


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Check each element until the target is found.
    for i in range(len(lst)):
        if lst[i] == target:
            return i

    # Linear search is O(n) because it may check every element.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    # Set the boundaries of the sorted list.
    left = 0
    right = len(lst) - 1

    # Continue while there are elements to search.
    while left <= right:

        # Find the middle element.
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle

        # Eliminate the left half if the target is larger.
        elif lst[middle] < target:
            left = middle + 1

        # Otherwise, eliminate the right half.
        else:
            right = middle - 1

    # Binary search is O(log n) because it halves the search space.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # A sorted list of student scores.
    small_scores = [55, 67, 72, 81, 90, 95]

    # Search for an existing score.
    print("Linear search for 81:",
          linear_search(small_scores, 81))

    print("Binary search for 81:",
          binary_search(small_scores, 81))

    # Both searches return -1 when the score is missing.
    print("Linear search for 100:",
          linear_search(small_scores, 100))

    print("Binary search for 100:",
          binary_search(small_scores, 100))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # Create a sorted dataset containing 100,000 values.
    large_scores = list(range(100000))
    target = 99999

    # Measure linear search execution time.
    start = perf_counter()
    linear_result = linear_search(large_scores, target)
    linear_time = perf_counter() - start

    # Measure binary search execution time.
    start = perf_counter()
    binary_result = binary_search(large_scores, target)
    binary_time = perf_counter() - start

    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    print("Linear search time:", linear_time)
    print("Binary search time:", binary_time)

    # Binary search is generally faster for large sorted datasets
    # because it eliminates half of the remaining values each time.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # An empty list should return -1 for both searches.
    empty_scores = []

    print("Empty list (linear):",
          linear_search(empty_scores, 81))

    print("Empty list (binary):",
          binary_search(empty_scores, 81))

    # A single-element list should return index 0 if found.
    single_score = [81]

    print("Single element (linear):",
          linear_search(single_score, 81))

    print("Single element (binary):",
          binary_search(single_score, 81))

    # Test values at the beginning and end of the list.
    print("First element (linear):",
          linear_search(small_scores, 55))

    print("Last element (binary):",
          binary_search(small_scores, 95))

    # ===============================
    # REAL-WORLD APPLICATION
    # ===============================

    print("\n=== STUDENT SCORE LOOKUP ===")

    # A teacher searches for a specific score.
    student_scores = [60, 70, 75, 80, 85, 90, 100]
    search_score = 85

    # Binary search efficiently locates the score.
    result = binary_search(student_scores, search_score)

    if result != -1:
        print("Student score found at index:", result)
    else:
        print("Student score not found.")


if __name__ == "__main__":
    main()
