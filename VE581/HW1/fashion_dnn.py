import tensorflow as tf
import numpy as np
import random

"""Loading dataset..."""

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
label_name = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print("Brief on training dataset:")
print("  Num of figures: {:d}".format(y_train.shape[0]))
print("  Size of figure: {:d}x{:d}".format(x_train.shape[1], x_train.shape[2]))
print("Brief on testing dataset:")
print("  Num of figures: {:d}".format(y_test.shape[0]))
print("  Size of figure: {:d}x{:d}".format(x_test.shape[1], x_test.shape[2]))

"""Building model..."""

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Flatten(input_shape=(x_train.shape[1], x_train.shape[2])))

model.add(tf.keras.layers.Dense(128, activation='relu'))

model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.summary()

"""Compiling model..."""

loc_optimizer = tf.keras.optimizers.Adam(lr=1e-3, )
loc_loss = tf.keras.losses.sparse_categorical_crossentropy
loc_metrics = ['sparse_categorical_accuracy']
model.compile(optimizer=loc_optimizer,loss=loc_loss,metrics=loc_metrics)

"""Fitting model..."""

model.fit(x_train.astype(np.float32), y_train.astype(np.float32), verbose = 1, batch_size = 128, epochs=16)

"""Evaluating model..."""

score = model.evaluate(x_test.astype(np.float32), y_test.astype(np.float32), verbose = 1)
print("Loss: ", score[0])
print("Accuracy: ", score[1])

"""Predicting..."""

print("Choosing 10 figures randomly from testing dataset: ")

idx = []
cnt = 0
while cnt < 10:
  loc_idx = random.randint(0, 10000)
  if loc_idx not in idx:
    idx.append(loc_idx)
    cnt = cnt + 1

pred = model.predict_classes(np.array([x_test[e] for e in idx]))

print("{:>8s}{:>18s}{:>18s}{:>12s}".format("Index", "Prediction", "Actual", "Judgement"))
for i in range(10):
  loc_idx = idx[i]
  loc_pred = label_name[pred[i]]
  loc_ans = label_name[y_test[idx[i]]]
  loc_judge = pred[i]== y_test[idx[i]]
  print("{:>8d}{:>18s}{:>18s}{:>12b}".format(loc_idx, loc_pred, loc_ans, loc_judge))