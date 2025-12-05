# Python Algorithms & Data Structures Study

This repository contains Python implementations of fundamental computer science algorithms, created as study material for a final exam. It focuses on recursion, sorting algorithms, searching, and Object-Oriented Programming (OOP) principles.

## 📂 Contents

### 1. Sorting Algorithms
Implementations of various sorting logic, ranging from simple $O(N^2)$ sorts to efficient $O(N \log N)$ recursive sorts.
* **Bubble Sort:** Swaps adjacent elements to "bubble" the largest value to the end. Optimized to stop early if no swaps occur.
* **Merge Sort:** A recursive divide-and-conquer algorithm that splits the list and merges sorted halves.
* **(Coming soon)Selection Sort:** Repeatedly finds the minimum element and moves it to the sorted section.
* **(Coming soon)Insertion Sort:** Builds the sorted array one item at a time by sliding elements.

### 2. Searching
* **Binary Search:** An $O(\log N)$ search algorithm that repeatedly divides the search interval in half. 
    * *Note:* Contains a helper function to ensure the array is sorted before searching.

### 3. Recursion Practice (Coming soon)
Solutions to recursive logic problems, including:
* **Palindrome Checker:** Verifies if a string reads the same forwards and backwards.
* **The "Beggars" Problem:** Distributing coins cyclically to a list of people.
* **Pair Counting:** Counting overlapping pairs of characters in a string.
* **Alternating Sums:** Calculating `(Sum of Evens) - (Sum of Odds)`.

## 🚀 How to Run

**Prerequisites**
* Python 3.x

**Running a Sort**
To run a specific algorithm (e.g., Bubble Sort), execute the file directly:
```bash
python3 bubble_sort.py
