import time

# The number of iterations to perform
ITERATIONS = 100000000

def calculate_pi():
    pi = 0.0
    sign = 1.0
    for i in range(1, ITERATIONS, 2):
        pi += sign / i
        sign = -sign
    return 4.0 * pi

start_time = time.time()

# Perform the calculation in a loop
while True:
    calculate_pi()

    # Check if the desired time has elapsed
    elapsed_time = time.time() - start_time
    if elapsed_time >= 60:  # Change the time limit as needed
        break
