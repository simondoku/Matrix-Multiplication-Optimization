#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#define MAX_THREADS 8

typedef struct {
    int **matrix1;
    int **matrix2;
    int **result;
    int start;
    int end;
} ThreadArgs;

void *matrix_multiply_worker(void *arg) {
    ThreadArgs *args = (ThreadArgs *)arg;
    int **matrix1 = args->matrix1;
    int **matrix2 = args->matrix2;
    int **result = args->result;
    int start = args->start;
    int end = args->end;

    for (int i = start; i < end; i++) {
        for (int j = 0; j < end; j++) {
            for (int k = 0; k < end; k++) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }

    return NULL;
}

int main() {
    int matrix_sizes[] = {10, 50, 100, 500};
    int thread_numbers[] = {1, 2, 4, 8};

    for (int size_index = 0; size_index < 4; size_index++) {
        for (int thread_index = 0; thread_index < 4; thread_index++) {
            int size = matrix_sizes[size_index];
            int num_threads = thread_numbers[thread_index];

            int **matrix1 = malloc(size * sizeof(int *));
            int **matrix2 = malloc(size * sizeof(int *));
            int **result = malloc(size * sizeof(int *));

            for (int i = 0; i < size; i++) {
                matrix1[i] = malloc(size * sizeof(int));
                matrix2[i] = malloc(size * sizeof(int));
                result[i] = malloc(size * sizeof(int));
            }

            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    matrix1[i][j] = 1;
                    matrix2[i][j] = 1;
                    result[i][j] = 0;
                }
            }

            pthread_t threads[MAX_THREADS];
            ThreadArgs thread_args[MAX_THREADS];
            int chunk_size = size / num_threads;

            clock_t start_time = clock();

            for (int i = 0; i < num_threads; i++) {
                thread_args[i].matrix1 = matrix1;
                thread_args[i].matrix2 = matrix2;
                thread_args[i].result = result;
                thread_args[i].start = i * chunk_size;
                thread_args[i].end = (i != num_threads - 1) ? (i + 1) * chunk_size : size;
                pthread_create(&threads[i], NULL, matrix_multiply_worker, &thread_args[i]);
            }

            for (int i = 0; i < num_threads; i++) {
                pthread_join(threads[i], NULL);
            }

            clock_t end_time = clock();

            printf("Matrix size: %d, Number of threads: %d, Execution time: %.2f seconds\n",
                   size, num_threads, (double)(end_time - start_time) / CLOCKS_PER_SEC);

            for (int i = 0; i < size; i++) {
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