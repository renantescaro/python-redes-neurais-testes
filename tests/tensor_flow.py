import tensorflow as tf

elu = tf.nn.elu(1.0)

print(elu.numpy())
print(type(elu))