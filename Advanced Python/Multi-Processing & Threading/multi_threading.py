'''
Multithreading

When to use:
-> Best for I/O bound tasks: (Tasks that spend more time waiting for I/O ops)
    -> reading files
    -> API calls
    -> DB Queries

Python threads run in the same memory spaces and 
are controlled by GIL(Global Interpreter Lock),
which limits performance in CPU-bound tasks

-> Concurrent Execution: to improve the throughput of the application
'''

import threading
import time
import requests

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'Number:{i}')

def print_letter():
    for letter in 'abcde':
        time.sleep(2)
        print(f'Letter: {letter}')
#create mltiple threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t = time.time()

# single thread ops
# print_numbers()
# print_letter()
#20.08949065208435

# start the threads
t1.start()
t2.start()

# wait for the thread to complete
t1.join()
t2.join()
#10.039688348770142

finished_time = time.time()-t
print(finished_time)