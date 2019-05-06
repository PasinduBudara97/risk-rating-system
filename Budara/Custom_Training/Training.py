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

class_names = ['Iris setosa','Iris versicolor','Iris virginica']

batch_size = 32
train_dataset = tf.contrib.data.make_csv_dataset(
    train_dataset_fp,
    batch_size,
    column_names=column_names,
    label_name=label_name,
    num_epochs=1
)
features, labels = next(iter(train_dataset))

features
plt.scatter(features['petal_length'].numpy(),
            features['sepal_length'].numpy(),
            c=labels.numpy(),
            cmap='viridis')

plt.xlabel("Petal length")
plt.ylabel("Sepal length")
print("done")
def pack_features_vector(features, labels):
  """Pack the features into a single array."""
  features = tf.stack(list(features.values()), axis=1)
  return features, labels

train_dataset = train_dataset.map(pack_features_vector)
features, labels = next(iter(train_dataset))

print(features[:5])