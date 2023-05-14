import time

ITERATIONS = 100000000

def calculate_pi():
    pi = 0.0
    sign = 1.0
    for i in range(1, ITERATIONS, 2):
        pi += sign / i
        sign = -sign
    return 4.0 * pi

start_time = time.time()

while True:
    calculate_pi()

    elapsed_time = time.time() - start_time
    if elapsed_time >= 60:
        break
