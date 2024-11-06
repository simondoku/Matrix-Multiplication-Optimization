#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

int **matrix1, **matrix2, **result;
int size;

void generate_matrices()
{
#pragma omp parallel for
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            matrix1[i][j] = 1;
            matrix2[i][j] = 1;
            result[i][j] = 0;
        }
    }
}

void matrix_multiply()
{
#pragma omp parallel for
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
    int thread_numbers[] = {1, 2, 4, 8};

    for (int size_index = 0; size_index < 4; size_index++)
    {
        for (int thread_index = 0; thread_index < 4; thread_index++)
        {
            size = matrix_sizes[size_index];
            int num_threads = thread_numbers[thread_index];

            matrix1 = malloc(size * sizeof(int *));
            matrix2 = malloc(size * sizeof(int *));
            result = malloc(size * sizeof(int *));

            for (int i = 0; i < size; i++)
            {
                matrix1[i] = malloc(size * sizeof(int));
                matrix2[i] = malloc(size * sizeof(int));
                result[i] = malloc(size * sizeof(int));
            }

            generate_matrices();

            omp_set_num_threads(num_threads);

            clock_t start_time = clock();
            matrix_multiply();
            clock_t end_time = clock();

            printf("Matrix size: %d, Number of threads: %d, Execution time: %.2f seconds\n",
                   size, num_threads, (double)(end_time - start_time) / CLOCKS_PER_SEC);

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
    }

    return 0;
}