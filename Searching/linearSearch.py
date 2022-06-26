def search(arr, n, x):
    # -1 means, element not in the list
    # algorithm returns the index
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1