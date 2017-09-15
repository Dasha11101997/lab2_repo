def find_min(arr):
    if arr:
        min = arr[0]
        for el in arr:
            if el < min:
                min = el
        return min
    else:
        print("Массив пуст")


def arifm(arr):
    if arr:
        summ = 0
        for el in arr:
            summ += el
        n = len(arr)
        return summ / n
    else:
        print("Массив пуст")


mass = [1, 4, 7, 24, 56, 76, 98, 2, 0]
print(find_min(mass))
mass1 = [1, 3, 20, 32, 44, 52, 76, 81, 99]
print(arifm(mass1))
