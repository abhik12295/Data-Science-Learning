# Multi-threading with Thread Pool Executer
'''
library : concurrent.futures
Simplifies thread management
 -> ideal for I/O outbound tasks with cleaner API
'''

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Square :{number**2}"

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]

if __name__=="__main__":
    with ThreadPoolExecutor(max_workers=3) as executer:
        results = executer.map(print_number, numbers)

    for result in results:
        print(result)