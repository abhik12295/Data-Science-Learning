'''
Real world example: Multiprocessing for CPU-bound tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers,
involve significant computational work.
Multiprocessing can be used to distribute the workload across multiple 
CPU cores, improve performance.
'''

import multiprocessing
import math
import sys
import time


# function to compute factorials of a given number
def compute_factorial(number):
    print(f'Computing factorial of {number}')
    result = math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result 

if __name__=="__main__":
    numbers = [5000,6000,7000,8000]
    start_time = time.time()

    #create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial,numbers)
    end_time = time.time()
    print(f'Results: {results}')
    print(f'Time taken: {end_time-start_time} seconds')


'''
Why use get_context("fork")?
    Normally, on Windows and Mac, multiprocessing uses spawn method by default, 
    which is slower (it starts a new Python interpreter for each process).

    "fork" is faster because it copies the parent process memory instantly 
    (only available on Unix/Linux/macOS — not Windows).

    You also get more control over how the processes are created

import multiprocessing
import math
import time

def compute_factorial(number):
    print(f'Computing factorial of {number}')
    result = math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result 

if __name__=="__main__":
    numbers = [5000, 6000, 7000, 8000]
    start_time = time.time()

    # Use 'fork' start method for faster process creation
    ctx = multiprocessing.get_context("fork")
    with ctx.Pool(processes=4) as pool:  # specify number of processes if you want
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()
    print(f'Results: {results}')
    print(f'Time taken: {end_time - start_time} seconds')

'''