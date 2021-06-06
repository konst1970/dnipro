from matplotlib import pyplot as plt
import tensorflow as tf
import numpy as np
import timeit

from tensorflow.python.framework import registry


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

@tf.function
def solve_tf(a, b):
    with tf.device('/gpu:0'):
        return tf.linalg.solve(a, b) 


def solve(a, b):
    return np.linalg.solve(a, b)


def test(sizes: list):
    np_times = []
    tf_times = []
    for size in sizes:
        a_np = np.random.randn(size, size)
        a_tf = tf.constant(a_np)
        b_np = np.random.randn(size, 1)
        b_tf = tf.constant(b_np)
        start_time = timeit.default_timer()
        res = solve(a_np, b_np)
        end_time = timeit.default_timer() - start_time
        np_times.append(end_time)
        print(f'{bcolors.WARNING}cpu: size - {size}, time - {end_time}. {bcolors.ENDC}')
        # print(res)

        start_time = timeit.default_timer()
        solve_tf(a_tf, b_tf)
        end_time = timeit.default_timer() - start_time
        tf_times.append(end_time)
        print(f'{bcolors.WARNING}gpu: size - {size}, time - {end_time}. {bcolors.ENDC}')
        # print(res)

    plt.plot(sizes,np_times,label='TensorFlow')
    plt.plot(sizes,tf_times,label='Numpy')
    plt.legend()
    plt.ylabel('Execution time')
    plt.xlabel('Matrix size')
    plt.show()


if __name__ == '__main__':
    sizes = [10, 100, 1000, 2000, 3000, 5000, 10000,]# 12000, 15000, 20000]
    test(sizes)