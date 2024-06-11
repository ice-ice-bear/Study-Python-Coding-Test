arr = [5, 3, 4, 7, 9, 2, 5, 3, 5]

arrMin = float('inf')

for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]

print(arrMin)