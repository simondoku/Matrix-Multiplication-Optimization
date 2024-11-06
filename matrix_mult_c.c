#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void multiply_matrices(int **matrix1, int **matrix2, int **result, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            for (int k = 0; k < size; k++)
            {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }
}

int main()
{
    int matrix_sizes[] = {10, 50, 100, 500};

    for (int size_index = 0; size_index < 4; size_index++)
    {
        int size = matrix_sizes[size_index];

        int **matrix1 = malloc(size * sizeof(int *));
        int **matrix2 = malloc(size * sizeof(int *));
        int **result = malloc(size * sizeof(int *));

        for (int i = 0; i < size; i++)
        {
            matrix1[i] = malloc(size * sizeof(int));
            matrix2[i] = malloc(size * sizeof(int));
            result[i] = malloc(size * sizeof(int));
        }

        for (int i = 0; i < size; i++)
        {
            for (int j = 0; j < size; j++)
            {
                matrix1[i][j] = 1;
                matrix2[i][j] = 1;
                result[i][j] = 0;
            }
        }

        clock_t start_time = clock();
        multiply_matrices(matrix1, matrix2, result, size);
        clock_t end_time = clock();

        printf("Matrix size: %d, Execution time: %.2f seconds\n",
               size, (double)(end_time - start_time) / CLOCKS_PER_SEC);

        for (int i = 0; i < size; i++)
        {
            free(matrix1[i]);
            free(matrix2[i]);
            free(result[i]);
        }

        free(matrix1);
        free(matrix2);
        free(result);
    }

    return 0;
}