import numpy as np
import time
def scalar_addition(first_array: np.ndarray, second_array: np.ndarray) -> float:
    start_time = time.time()
    final_array = np.zeros(len(first_array), dtype=np.float32)
    for index in range(len(first_array)):
       final_array = first_array[index] + second_array[index]
    end_time = time.time()
    scalar_time = end_time - start_time
    print(f"Scalar addition time: {scalar_time:.5f} seconds")
    return scalar_time

def vectorized_addition(first_array: np.ndarray, second_array: np.ndarray) -> float:
    start_time = time.time()
    final_array = first_array + second_array
    end_time = time.time()
    vectorized_time = end_time - start_time
    print(f"Vectorized addition time: {vectorized_time:.5f} seconds")
    return vectorized_time

def generate_array(number_of_elements:int) -> np.ndarray:
    return np.random.rand(number_of_elements).astype(np.float32)
if __name__ =="__main__":
  number_of_elements = 10**6
  first_array = generate_array(number_of_elements)
  second_array = generate_array(number_of_elements)

  scalar_time = scalar_addition(first_array, second_array)
  vectorized_time = vectorized_addition(first_array, second_array)
  print(f"Performance improvement: {scalar_time / vectorized_time:.2f}x")

