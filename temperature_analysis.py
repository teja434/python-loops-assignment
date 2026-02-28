import numpy as np
import time

temps_celsius = np.array([22, 25, 28, 24, 26])
temps_fahrenheit = temps_celsius * 1.8 + 32
avg_fahrenheit = round(np.mean(temps_fahrenheit), 1)

print("Task 1 Results:")
print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)
print("Average Fahrenheit:", avg_fahrenheit)


scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print("\nTask 2 Results:")
print("Shape:", scores.shape)
print("Total elements:", scores.size)
highest = np.max(scores)
lowest = np.min(scores)
range_score = highest - lowest
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Range:", range_score)


numpy_array = np.arange(1, 50001)
python_list = list(range(1, 50001))

start_numpy = time.time()
numpy_sum = np.sum(numpy_array)
end_numpy = time.time()
numpy_time = end_numpy - start_numpy
start_python = time.time()
python_sum = sum(python_list)
end_python = time.time()
python_time = end_python - start_python

speed_ratio = python_time / numpy_time

print("\nTask 3 Results:")
print("NumPy sum:", numpy_sum)
print("Python sum:", python_sum)
print(f"NumPy time: {numpy_time:.4f} seconds")
print(f"Python time: {python_time:.4f} seconds")
print(f"NumPy is {speed_ratio:.1f}x faster")