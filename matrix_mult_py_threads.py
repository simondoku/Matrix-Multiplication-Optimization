import threading
import multiprocessing
import time


def generate_matrix(rows, cols):
    return [[1 for _ in range(cols)] for _ in range(rows)]


def create_empty_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def matrix_multiply_worker(matrix1, matrix2, result, start, end):
    for i in range(start, end):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]


def matrix_multiply_with_threads(matrix1, matrix2, num_threads, start, end):
    num_cores = min(num_cores, len(matrix1))
    result = create_empty_matrix(end - start, len(matrix2[0]))

    threads = []
    chunk_size = (end - start) // num_threads
    for i in range(num_threads):
        thread_start = start + i * chunk_size
        thread_end = start + (i + 1) * chunk_size if i != num_threads - 1 else end
        thread = threading.Thread(
            target=matrix_multiply_worker,
            args=(matrix1, matrix2, result, thread_start, thread_end),
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result


def matrix_multiply_with_nodes(matrix1, matrix2, num_nodes, num_cores):
    num_nodes = min(num_nodes, len(matrix1))  # Add this line
    with multiprocessing.Manager() as manager:
        result = manager.list(
            [manager.list([0] * len(matrix2[0])) for _ in range(len(matrix1))]
        )

        processes = []
        chunk_size = len(matrix1) // num_nodes
        for i in range(num_nodes):
            node_start = i * chunk_size
            node_end = (i + 1) * chunk_size if i != num_nodes - 1 else len(matrix1)
            process = multiprocessing.Process(
                target=matrix_multiply_with_threads,
                args=(matrix1, matrix2, num_cores, node_start, node_end),
            )
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        return result


def main():
    matrix_sizes = [10, 50, 100, 500, 1000, 2000]  # Added 1000 and 2000
    node_numbers = [1, 2, 4, 8, 16, 32]  # Added 16 and 32
    core_numbers = [1, 2, 4, 8, 16, 32]  # Added 16 and 32

    # ... rest of the code remains the same ...

    for size in matrix_sizes:
        for num_nodes in node_numbers:
            for num_cores in core_numbers:
                matrix1 = generate_matrix(size, size)
                matrix2 = generate_matrix(size, size)

                start_time = time.time()
                result = matrix_multiply_with_nodes(
                    matrix1, matrix2, num_nodes, num_cores
                )
                end_time = time.time()

                print(
                    f"Matrix size: {size}, Number of nodes: {num_nodes}, Number of cores per node: {num_cores}, Execution time: {end_time - start_time} seconds"
                )


if __name__ == "__main__":
    main()
