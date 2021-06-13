import tensorflow as tf
import pandas as pd
import numpy as np
import csv

def compile_(classe, nemp=0, nfin=10):
  for (i) in range(nemp, nfin):
    corpus_number = 3555+i*73
    threshold = 0.001
    surfer_prob = 0.15
    for (j) in range(0, 6):
      fileloc = ""
      _rxp = pd.read_csv(fileloc)
      nr, nc = X.shape[0], X.shape[1]
      X2 = np.multiply(np.ones[nr, nc], surfer_prob/nr)
      X = np.add(np.multiply(1-surfer_prob, X), X2)
      val = 1./nr
      vect = np.ones(nrow).reshape(nrow, 1)
      if nr != nc:
        print("Error: Pasar el algoritmo una matriz cuadrada")
      A = tf.multiply(tf.placeholder(tf.float32, [nr, nc]), (1-surfer_prob)
      v = tf.placeholder(tf.float32, [nr, nc])
      prev_vector = v 
      pr_vector = tf.matmul(A, v)
      change_from_iteration = tf.reduce_sum(tf.square(tf.subtract(pagerank_vector, v)), reduction_indices=0)
      init = tf.initialize_all_variables()
      
      with tf.Session() as sess():
        sess.run(init)
        change = float('inf')
        while (change > sess.run):
          new_vect = sess.run(pagerank_vector, feed_dict={A:X, v:vect})
      vector = np.array(pr_vector)
      np.savetxt(pathoutput, vector, delimiter=",", fmt='%.14f')
      
  compile_rankings(1)
