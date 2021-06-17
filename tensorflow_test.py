from utility import create_array
from matplotlib import pyplot as plt
import re
import tensorflow as tf
import numpy as np
import timeit
import random

n = 10000

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def create_matrix(size, a, b):
    arr1 = [[random.random()*b + a for col in range(size)] for row in range(size)]
    arr2 = [[random.random()*b + a] for row in range(size)]
    return arr1, arr2


def solve_tf(size):
    with tf.device('/gpu:0'):
        arr1 = np.random.randint(low=-1, high=1, size=(size, size))
        arr2 = np.random.randint(low=-1, high=1, size=(size, 1))
        a = tf.convert_to_tensor(arr1, dtype=tf.dtypes.float32)
        b = tf.convert_to_tensor(arr2, dtype=tf.dtypes.float32)

        start_time = timeit.default_timer()
        r = tf.linalg.solve(a, b)
        end_time = timeit.default_timer() - start_time

        return end_time


def solve(size):
    arr1 = np.random.randint(low=-1, high=1, size=(size, size))
    arr2 = np.random.randint(low=-1, high=1, size=(size, 1))

    start_time = timeit.default_timer()
    r = np.linalg.solve(arr1, arr2)
    end_time = timeit.default_timer() - start_time

    return end_time


def test(sizes: list):
    np_times = []
    tf_times = []
    for size in sizes:
    # start_time = timeit.default_timer()
        end_time = solve(size)
    # end_time = timeit.default_timer() - start_time
        np_times.append(end_time)
        print(f'{bcolors.WARNING}cpu: size - {size}, time - {end_time}. {bcolors.ENDC}')

    # start_time = timeit.default_timer()
        end_time = solve_tf(size)
    # end_time = timeit.default_timer() - start_time
        tf_times.append(end_time)
        print(f'{bcolors.WARNING}gpu: size - {size}, time - {end_time}. {bcolors.ENDC}')

    plt.plot(sizes,np_times,label='Numpy')
    plt.plot(sizes,tf_times,label='TensorFlow')
    plt.legend()
    plt.ylabel('Execution time')
    plt.xlabel('Matrix size')
    plt.show()


if __name__ == '__main__':
    sizes = [1000, 2000, 3000, 5000, 10000,]# 12000, 15000, 20000]
    test(sizes)