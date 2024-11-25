import multiprocessing
import time

def quick_sort(arr):
    """
    Perform quick sort on the input array.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def parallel_quick_sort(arr):
    """
    Perform parallel quick sort on the input array.
    """
    if len(arr) <= 1:
        return arr
    
    # Split the array
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Create a pool of worker processes
    left_sorted, right_sorted = multiprocessing.Pool().map(quick_sort, [left, right])
    
    return left_sorted + middle + right_sorted

if __name__ == "__main__":
    import random

    # Generate a random array
    size = 1000  # Change this to a larger value for testing
    array = [random.randint(0, 10000) for _ in range(size)]
    # print(f"Original array: {array}")
    
    # Perform both serial and parallel quick sorts

    serial_start = time.time()
    serial_sorted_array = quick_sort(array[:])
    serial_end = time.time()
    
    parallel_start = time.time()
    parallel_sorted_array = parallel_quick_sort(array[:])
    parallel_end = time.time()
    
    print(f"Time taken for serial quick sort: {serial_end - serial_start:.6f} seconds")
    print(f"Time taken for parallel quick sort: {parallel_end - parallel_start:.6f} seconds")

# Time taken for serial quick sort: 408.052842 seconds
# Time taken for parallel quick sort: 191.655397 seconds


