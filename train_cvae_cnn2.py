import os
import tensorflow as tf
from util import mnist_train
from model import CVAE_CNN2

if __name__ == '__main__':
    # Ignore warning message by tensor flow
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    save_path = "./log/cvae_cnn2/"
    network_architecture = dict(n_input=[28, 28, 1], n_z=20)
    model = CVAE_CNN2(10, network_architecture=network_architecture, batch_size=100, save_path=save_path,
                      learning_rate=0.001, activation=tf.nn.relu)
    mnist_train(model=model, epoch=200, save_path=save_path, mode="conditional", input_image=True)