#!/bin/bash
#SBATCH --job-name=pa3_job # Job name
#SBATCH --mail-type=END,FAIL # Mail events (NONE, BEGIN, END,FAIL, ALL)
#SBATCH --mail-user=email@ufl.edu # Where to send mail
#SBATCH --nodes=1 # Run all processes on a single node
#SBATCH --ntasks=1 # Run a single task
#SBATCH --cpus-per-task=4 # Number of CPU cores per task
#SBATCH --mem=1gb # Job memory request
#SBATCH --time=00:15:00 # Time limit hrs:min:sec
#SBATCH --output=pa3_%j.log # Standard output and error log
pwd; hostname; date

#Compile Python Program without threads
echo "Compiling Python program without threads..."
python matrix_mult_py.py

# Execute Python program with threads
echo "Executing Python program with threads..."
python matrix_mult_py_threads.py

# Compile C program without threads
gcc -std=c99 -o matrix_mult_c matrix_mult_c.c

# Execute C program without threads
echo "Executing C program without threads"
./matrix_mult_c

# Compile C program with POSIX threads
gcc -std=c99 -o matrix_mult_c_threads matrix_mult_c_threads.c -lpthread

# Execute C program with POSIX threads
echo "Executing C program with POSIX threads"
./matrix_mult_c_threads

# Compile C program with OpenMP
gcc -std=c99 -o matrix_mult_c_openmp matrix_mult_c_openmp.c -fopenmp

# Execute C program with OpenMP
echo "Executing C program with OpenMP..."
./matrix_mult_c_openmp

module load python
