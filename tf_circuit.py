import tensorflow as tf

A = tf.constant([[1,1,1],
                 [1,5,5],
                 [1,5,13]], dtype = tf.float32)
b = tf.constant([3,11,20], shape = (3,1), dtype = tf.float32)
lu, p = tf.linalg.lu(A)   # Factorization result of LU
x_sol_lu = tf.linalg.lu_solve(lu,p,b)
x_sol_lu