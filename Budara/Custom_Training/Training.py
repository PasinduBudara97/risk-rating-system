from __future__ import absolute_import,division,print_function
import os
import matplotlib.pyplot as plt
import tensorflow as tf

tf.enable_eager_execution()

print("Tensorflow version: {}".format(tf.__version__))
#print("Eager execution: {}".format(tf.executing_eagerly))


train_data_url="https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"
train_dataset_fp = tf.keras.utils.get_file(fname=os.path.basename(train_data_url),origin=train_data_url)

print("Local copy of the dataset file: {}".format(train_dataset_fp))
#train_dataset_fp.head()

# column order in CSV file
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

feature_names = column_names[:-1]
label_name = column_names[-1]

print("Features: {}".format(feature_names))
print("Label: {}".format(label_name))