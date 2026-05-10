Empirical Analysis of Sorting AlgorithmsThis project provides a comparative study of four fundamental sorting algorithms.
It evaluates their performance based on execution time and space complexity across different input sizes and initial data orderings (Sorted vs. Reverse Sorted).

🚀 Algorithms Implemented
The following algorithms were implemented from scratch in Python:
Selection Sort: O(n^2) time  O(1) space.
Bubble Sort: O(n^2) time | O(1) space (with early-exit optimization)
.Quick Sort: O(n \log n) average time | O(\log n) space (Lomuto partition).
Merge Sort: O(n \log n) time | O(n) space.

📊 Experimental 
SetupLanguage: Python 3.x
Trials: Each case was run 3 times, and the average time was recorded using time.perf_counter().
Test Cases:Small Dataset: Size 5 (Sorted & Reverse Sorted)Large Dataset: Size 100 (Sorted & Reverse Sorted)
