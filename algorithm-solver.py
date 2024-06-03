from bisect import bisect_left

# Define the available algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

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

# Display the menu and get the user's choice
def display_menu():
    print("Choose an algorithm:")
    print("1. Bubble Sort")
    print("2. Binary Search")
    print("3. Fibonacci Search")
    choice = int(input("Enter the number of your choice: "))
    return choice

# Execute the chosen algorithm based on user input
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

# Main function
def main():
    choice = display_menu()
    execute_algorithm(choice)

# Run the main function
if __name__ == "__main__":
    main()
