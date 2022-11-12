from keras.datasets import mnist
from matplotlib import pyplot as plt
from tensorflow.python.keras.utils.np_utils import to_categorical


def load_dataset():
    # load Mnist dataset
    (train_X, train_Y), (test_X, test_Y) = mnist.load_data()
    # reshape dataset to have a single channel
    train_X = train_X.reshape((train_X.shape[0], 28, 28, 1))
    test_X = test_X.reshape((test_X.shape[0], 28, 28, 1))
    # one hot encode target values
    train_Y = to_categorical(train_Y)
    test_Y = to_categorical(test_Y)
    for i in range(9):
        plt.subplot(330 + 1 + i)
        plt.imshow(train_X[i], cmap=plt.get_cmap('gray'))
    plt.show()
    return train_X, train_Y, test_X, test_Y
