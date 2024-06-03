# Multi-Algorithm Solver using Python

This repository contains implementations of various algorithms including Bubble Sort, Binary Search, and Fibonacci Search. Additionally, a simple command-line interface (CLI) is provided to allow users to choose and execute these algorithms on their input data.

## Algorithms

### Bubble Sort
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

### Binary Search
Binary Search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### Fibonacci Search
Fibonacci Search is a comparison-based technique that uses Fibonacci numbers to divide the array into sub-arrays, making the search process efficient in sorted arrays.

```python
def fibMonaccianSearch(arr, x, n):
    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm2 + fibMMm1
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
    offset = -1
    while (fibM > 1):
        i = min(offset + fibMMm2, n-1)
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i
    if(fibMMm1 and arr[n-1] == x):
        return n-1
    return -1
```

## Usage

### Menu and Execution

A simple CLI menu is provided to allow users to select an algorithm and provide input data. The program will then execute the selected algorithm and display the results.

```python
def display_menu():
    print("Choose an algorithm:")
    print("1. Bubble Sort")
    print("2. Binary Search")
    print("3. Fibonacci Search")
    choice = int(input("Enter the number of your choice: "))
    return choice

def execute_algorithm(choice):
    if choice == 1:
        arr = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
        sorted_arr = bubble_sort(arr)
        print(f"Sorted array: {sorted_arr}")
    elif choice == 2:
        arr = list(map(int, input("Enter a sorted list of numbers separated by spaces: ").split()))
        target = int(input("Enter the number to search for: "))
        result = binary_search(arr, target)
        if result != -1:
            print(f"Element found at index: {result}")
        else:
            print("Element not found in the array")
    elif choice == 3:
        arr = list(map(int, input("Enter a sorted list of numbers separated by spaces: ").split()))
        target = int(input("Enter the number to search for: "))
        n = len(arr)
        result = fibMonaccianSearch(arr, target, n)
        if result != -1:
            print(f"Element found at index: {result}")
        else:
            print("Element not found in the array")
    else:
        print("Invalid choice!")

def main():
    choice = display_menu()
    execute_algorithm(choice)

if __name__ == "__main__":
    main()
```

## How to Run
1. Clone the repository.
2. Navigate to the directory containing the script.
3. Run the script using Python:
   ```bash
   python script_name.py
   ```
4. Follow the on-screen instructions to choose an algorithm and provide input data.
