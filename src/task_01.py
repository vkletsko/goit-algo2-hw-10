import random
import time
import matplotlib.pyplot as plt

# Детермінований QuickSort


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# Рандомізований QuickSort


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def measure_exec_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time


def draw_graph(randomized_results, deterministic_results):
    sizes = [size for size, _ in deterministic_results]
    deterministic_times = [time for _, time in deterministic_results]
    randomized_times = [time for _, time in randomized_results]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, deterministic_times,
             label='Детермінований QuickSort', marker='o')
    plt.plot(sizes, randomized_times,
             label='Рандомізований QuickSort', marker='o')

    plt.title("Порівняння часу виконання алгоритмів QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 500_000]
    test_arrays = {size: [random.randint(
        0, 1_000_000) for _ in range(size)] for size in sizes}
    deterministic_results = []
    randomized_results = []

    print("\n Порівняння ефективності QuickSort алгоритмів")

    for size, arr in test_arrays.items():
        print(f"\nРозмір масиву: {size}")

        # Детермінований QuickSort
        deterministic_times = []
        for _ in range(5):
            arr_copy = arr[:]
            deterministic_times.append(measure_exec_time(
                deterministic_quick_sort, arr_copy))
        avg_deterministic_time = sum(
            deterministic_times) / len(deterministic_times)
        deterministic_results.append((size, avg_deterministic_time))
        print(
            f"Детермінований QuickSort: середній час {avg_deterministic_time:.4f} секунд")

        # Рандомізований QuickSort
        randomized_times = []
        for _ in range(5):
            arr_copy = arr[:]
            randomized_times.append(measure_exec_time(
                randomized_quick_sort, arr_copy))
        avg_randomized_time = sum(randomized_times) / len(randomized_times)
        randomized_results.append((size, avg_randomized_time))
        print(
            f"Рандомізований QuickSort: середній час {avg_randomized_time:.4f} секунд")

    draw_graph(randomized_results, deterministic_results)
