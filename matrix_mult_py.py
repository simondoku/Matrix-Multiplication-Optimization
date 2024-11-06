import time

def generate_matrix(rows, cols):
    return [[1 for _ in range(cols)] for _ in range(rows)]

def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError(
            "Number of columns in the first matrix must be equal to the number of rows in the second matrix"
        )

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def main():
    matrix_sizes = [10, 50, 100, 500]

    for size in matrix_sizes:
        matrix1 = generate_matrix(size, size)
        matrix2 = generate_matrix(size, size)

        start_time = time.time()
        result = matrix_multiply(matrix1, matrix2)
        end_time = time.time()

        print(f"Matrix size: {size}, Execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()