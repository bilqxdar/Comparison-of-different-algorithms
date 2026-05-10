import time

# Selection Sort 
def Selection_Sort(data):
    size = len(data)
    for i in range(size):
        # find the index of the lowest value
        lowest = i
        for j in range(i + 1, size):
            if data[j] < data[lowest]:
                lowest = j
        # swap using a temporary variable
        val_holder = data[i]
        data[i] = data[lowest]
        data[lowest] = val_holder
    return data

# Bubble Sort 
def BubbleSort_Algo(data):
    length = len(data)
    for p in range(length):
        for q in range(0, length - p - 1):
            if data[q] > data[q + 1]:
                # basic swap logic
                tmp_val = data[q]
                data[q] = data[q + 1]
                data[q + 1] = tmp_val
    return data

# Quick Sort 
def Quick_Sort_Function(arr):
    if len(arr) <= 1:
        return arr
    else:
        # picking the first item as the pivot
        piv = arr[0]
        smaller = []
        bigger = []
        for x in range(1, len(arr)):
            if arr[x] <= piv:
                smaller.append(arr[x])
            else:
                bigger.append(arr[x])
        return Quick_Sort_Function(smaller) + [piv] + Quick_Sort_Function(bigger)

# Merge Sort 
def MergeSortAlg(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        leftSide = arr[:middle]
        rightSide = arr[middle:]

        MergeSortAlg(leftSide)
        MergeSortAlg(rightSide)

        a = b = c = 0
        
        while a < len(leftSide) and b < len(rightSide):
            if leftSide[a] < rightSide[b]:
                arr[c] = leftSide[a]
                a += 1
            else:
                arr[c] = rightSide[b]
                b += 1
            c += 1

        while a < len(leftSide):
            arr[c] = leftSide[a]
            a += 1
            c += 1

        while b < len(rightSide):
            arr[c] = rightSide[b]
            b += 1
            c += 1
    return arr


def measure_time(label, sort_func, array_data):
    combined_time = 0
    for cycle in range(3):
        # use a list copy to keep the original data unsorted
        fresh_data = list(array_data) 
        start_t = time.time()
        sort_func(fresh_data)
        end_t = time.time()
        combined_time += (end_t - start_t)
    
    average_result = combined_time / 3
    print(f"{label} -> Result: {average_result}")


arr5_up = [1, 2, 3, 4, 5]
arr5_down = [5, 4, 3, 2, 1]
arr100_up = list(range(1, 101))
arr100_down = list(range(100, 0, -1))

all_data = [arr5_up, arr5_down, arr100_up, arr100_down]
test_labels = ["5-Sorted", "5-Reverse", "100-Sorted", "100-Reverse"]


print("=== SELECTION SORT DATA ===")
for i in range(4):
    measure_time(test_labels[i], Selection_Sort, all_data[i])

print("\n=== BUBBLE SORT DATA ===")
for i in range(4):
    measure_time(test_labels[i], BubbleSort_Algo, all_data[i])

print("\n=== QUICK SORT DATA ===")
for i in range(4):
    measure_time(test_labels[i], Quick_Sort_Function, all_data[i])

print("\n=== MERGE SORT DATA ===")
for i in range(4):
    measure_time(test_labels[i], MergeSortAlg, all_data[i])