num1 = 6
num2 = 3

print(num1 + num2)

# bubble sort algorithm
def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

test_list = [3, 5, 1, 2, 4]

print(bubble_sort(test_list))
