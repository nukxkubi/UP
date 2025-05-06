import random


def task1():
    print("\nЗадание 1:")
    n = int(input("Введите размер массива: "))
    arr = [random.uniform(-5, 5) for _ in range(n)]
    print("Исходный массив:", [round(x, 2) for x in arr])

    # 1. Сумма элементов с нечетными номерами (индексами 0, 2, 4...)
    sum_odd = sum(arr[i] for i in range(0, n, 2))
    print("1. Сумма элементов с нечетными номерами:", round(sum_odd, 2))

    # 2. Сумма между первым и последним отрицательными элементами
    first_neg = next((i for i, x in enumerate(arr) if x < 0), None)
    last_neg = next((i for i, x in enumerate(reversed(arr)) if x < 0), None)

    if first_neg is not None and last_neg is not None:
        last_neg = len(arr) - 1 - last_neg
        if first_neg < last_neg:
            sum_between = sum(arr[first_neg + 1:last_neg])
            print("2. Сумма между первым и последним отрицательными:", round(sum_between, 2))
        else:
            print("2. Нет элементов между первым и последним отрицательными")
    else:
        print("2. В массиве нет отрицательных элементов")

    # 3. Сжать массив
    compressed = [x for x in arr if abs(x) > 1]
    zeros = [0] * (n - len(compressed))
    compressed += zeros
    print("3. Сжатый массив:", [round(x, 2) for x in compressed])


def task2():
    print("\nЗадание 2:")
    n = int(input("Введите размер массива: "))
    arr = [random.uniform(-5, 5) for _ in range(n)]
    print("Исходный массив:", [round(x, 2) for x in arr])

    # 1. Количество нулевых элементов
    zero_count = sum(1 for x in arr if x == 0)
    print("1. Количество нулевых элементов:", zero_count)

    # 2. Сумма после минимального элемента
    min_index = arr.index(min(arr))
    if min_index < len(arr) - 1:
        sum_after_min = sum(arr[min_index + 1:])
        print("2. Сумма после минимального элемента:", round(sum_after_min, 2))
    else:
        print("2. Минимальный элемент последний, сумма после него: 0")

    # 3. Сортировка по возрастанию модулей
    sorted_arr = sorted(arr, key=lambda x: abs(x))
    print("3. Массив, отсортированный по модулям:", [round(x, 2) for x in sorted_arr])


def main():
    print("Выберите задание (1 или 2):")
    choice = input("Введите номер задания: ")
    if choice == '1':
        task1()
    elif choice == '2':
        task2()
    else:
        print("Неверный выбор")


if __name__ == "__main__":
    main()