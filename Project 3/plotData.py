import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Parameters
num_threads = np.array([50, 200, 350, 500, 650])
num_cores = np.array([5, 15, 25])
matrix_sizes = np.array([100, 400, 700])

# Sample data generation
def generate_data(program_name):
    data = []
    times = []
    for n_threads in num_threads:
        for n_cores in num_cores:
            for size in matrix_sizes:
                # Generate data based on program
                if program_name == "Python_no_threads":
                    time = 10.0 / (n_cores * size / 1000)
                    # print(time)
                elif program_name == "Python_threads":
                    time = 5.0 / (n_threads * n_cores * size / 1000)
                    # print(time)

                elif program_name == "C_no_threads":
                    time = 2.0 / (n_threads * n_cores * size / 1000)
                    # print(time)

                elif program_name == "C_threads":
                    time = 1.0 / (n_threads * n_cores * size / 1000)
                    # print(time)

                elif program_name == "C_openmp":
                    time = 0.5 / (n_threads * n_cores * size / 1000)
                    # print(time)

                data.append([n_threads, n_cores, size])
                times.append(time)
    return data, times

# Generate data for each program
python_no_threads_data, python_no_threads_times = generate_data("Python_no_threads")
python_threads_data, python_threads_times = generate_data("Python_threads")
c_no_threads_data, c_no_threads_times = generate_data("C_no_threads")
c_threads_data, c_threads_times = generate_data("C_threads")
c_openmp_data, c_openmp_times = generate_data("C_openmp")
from mpl_toolkits.mplot3d import Axes3D

# Create figure and subplots
fig = plt.figure(figsize=(16, 8))
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232, projection='3d')
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234, projection='3d')
ax5 = fig.add_subplot(235, projection='3d')

# Helper function to plot data
def plot_data(ax, data, times, title, is_3d=False):
    x, y, z = zip(*data)
    if is_3d:
        scatter = ax.scatter(x, y, z, c=times, cmap='viridis_r')
        ax.set_zlabel("Number of Iterations")
    else:
        scatter = ax.scatter(x, y, c=times, cmap='viridis_r')
    ax.set_title(title)
    ax.set_xlabel("Number of Cores")
    ax.set_ylabel("Matrix Size")
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label("Processing Time")

# Plot data for each program
plot_data(ax1, python_no_threads_data, python_no_threads_times, "Python without threads")
plot_data(ax2, python_threads_data, python_threads_times, "Python with threads", is_3d=True)
plot_data(ax3, c_no_threads_data, c_no_threads_times, "C without threads")
plot_data(ax4, c_threads_data, c_threads_times, "C with threads", is_3d=True)
plot_data(ax5, c_openmp_data, c_openmp_times, "C with OpenMP", is_3d=True)

plt.tight_layout()
plt.show()