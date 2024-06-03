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

def getInvCount(arr, n): 
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count 

def knapsack(capacity, weights, values, counter):
    if counter == 0 or capacity == 0:
        return 0
    if weights[counter - 1] > capacity:
        return knapsack(capacity, weights, values, counter - 1)
    else:
        left_capacity = capacity - weights[counter - 1]
        new_value_included = values[counter - 1] + knapsack(left_capacity, weights, values, counter - 1)
        without_new_value = knapsack(capacity, weights, values, counter - 1)
        return max(new_value_included, without_new_value)

# Display the menu and get the user's choice
def display_menu():
    print("Choose an algorithm:")
    print("1. Bubble Sort")
    print("2. Binary Search")
    print("3. Fibonacci Search")
    print("4. Count Inversions")
    print("5. 0/1 Knapsack Problem")
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
    elif choice == 4:
        arr = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
        n = len(arr)
        inv_count = getInvCount(arr, n)
        print(f"Number of inversions are: {inv_count}")
    elif choice == 5:
        N = int(input("Enter the number of items (N): "))
        W = int(input("Enter the capacity of the knapsack (W): "))
        profits = list(map(int, input("Enter the profits separated by spaces: ").split()))
        weights = list(map(int, input("Enter the weights separated by spaces: ").split()))
        max_profit = knapsack(W, weights, profits, N)
        print(f"Output: {max_profit}")
        print(f"Explanation: There are items which have weight less than or equal to {W}. The maximum possible profit is {max_profit}.")
    else:
        print("Invalid choice!")

# Main function
def main():
    choice = display_menu()
    execute_algorithm(choice)

# Run the main function
if __name__ == "__main__":
    main()
