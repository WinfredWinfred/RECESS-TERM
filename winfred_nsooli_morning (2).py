#Assignment A7
#1a)show a context manager for file handling that automatically opens and closes a file using python
#Context managers are objects that can be used in Python's with statements.
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Example usage
with FileManager('example.txt', 'w') as file:
    file.write('Hello, world!')


    #b)show a context manager for managing a database connection
import sqlite3
from contextlib import contextmanager

@contextmanager
def db_connection(database):
    connection = sqlite3.connect(database)
    try:
        yield connection
    finally:
        connection.close()

# Example usage
with db_connection('mydatabase.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mytable")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


#c)show a multithreading and multiprocessing that allows us to run the function for different amounts of time
import time
import threading
import multiprocessing

# Function to run for a specified duration
def run_function(duration):
    print(f"Function will run for {duration} seconds")
    time.sleep(duration)
    print(f"Function finished after {duration} seconds")

# Example using multithreading
def run_with_threads():
    durations = [10, 12, 13, 14, 15]  # Different durations for the function

    threads = []
    for duration in durations:
        t = threading.Thread(target=run_function, args=(duration,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

# Example using multiprocessing
def run_with_processes():
    durations = [10,12, 13, 14, 15]  # Different durations for the function

    processes = []
    for duration in durations:
        p = multiprocessing.Process(target=run_function, args=(duration,))
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

# Run the examples
print("The threads are running:")
run_with_threads()

print("\nThe threads are running:")
run_with_processes()