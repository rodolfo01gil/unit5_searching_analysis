# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compared linear search and binary search
using Python.

I implemented both algorithms and tested their ability
to locate student scores in sorted lists.

The program demonstrated search efficiency, edge cases,
and a practical student score lookup application.

## Learning Objectives

- Implemented linear search
- Implemented binary search
- Compared search performance
- Analyzed algorithm efficiency

## Requirements

### 1. Small Dataset

I created a sorted list of student scores:

[55, 67, 72, 81, 90, 95]

I tested both algorithms using the scores 81 and 100.

Both algorithms returned index 3 when searching for 81.

Both algorithms returned -1 when searching for 100
because the score was not present.

### 2. Large Dataset

I created a sorted list containing 100,000 integers.

I searched for the value 99999 using both algorithms.

Both algorithms returned the correct index.

I measured their execution times using Python's
perf_counter() function.

Binary search required fewer comparisons because
it repeatedly divided the remaining search range in half.

### 3. Edge Cases

I tested the following edge cases:

- Empty list
- Single-element list
- Missing values
- First element
- Last element

Both algorithms returned -1 when searching an empty list.

Both algorithms returned index 0 when searching for
81 in a single-element list containing 81.

The boundary tests also returned the correct indices.

### 4. Performance Analysis

Linear search examined elements sequentially.

Its worst-case time complexity was O(n).

Binary search repeatedly eliminated half of the
remaining elements.

Its worst-case time complexity was O(log n).

Binary search was more efficient for large sorted
datasets because it required fewer comparisons.

However, linear search remained useful for small
or unsorted collections.

### 5. Real-World Application

I created a student score lookup example.

The application searched a sorted list of student
scores for the value 85.

Binary search successfully located the score and
returned its index.

This demonstrated how searching algorithms could
be used in student information systems.

## Implementation Approach

I used Python lists to store student scores.

For linear search, I used a for loop to examine
each element until a match was found.

For binary search, I used left, right, and middle
indices to repeatedly reduce the search range.

Both methods returned -1 when the target was absent.

I also added comments explaining how the algorithms
worked and why their performance differed.

## Discussion Board Reflection

This assignment helped me understand how data
organization affects searching efficiency.

I learned that linear search works with unsorted
data, while binary search requires sorted data.

Linear search was easier to implement because it
only required a loop and a comparison.

Binary search required more attention because
the search boundaries needed to be updated correctly.

I tested empty lists, single-element lists, and
boundary values to verify that both algorithms
handled different situations.

For large sorted datasets, binary search was the
better option because it eliminated half of the
remaining values after each comparison.

However, linear search remained useful when
working with small or unsorted datasets.

## Conclusion

I successfully implemented and compared linear
search and binary search in Python.

The assignment demonstrated how algorithm selection
affects efficiency and why testing edge cases is
important when developing reliable software.
