# plot diagnostic learning curves
from matplotlib import pyplot as plt
from numpy import std, mean


def summarize_diagnostics(history):
    for i in range(len(history)):
        # plot loss
        plt.subplot(2, 1, 1)
        plt.title('Cross Entropy Loss')
        plt.plot(history[i].history['loss'], color='blue', label='train')
        plt.plot(history[i].history['val_loss'], color='orange', label='test')
        # plot accuracy
        plt.subplot(2, 1, 2)
        plt.title('Accuracy')
        plt.plot(history[i].history['accuracy'], color='blue', label='train')
        plt.plot(history[i].history['val_accuracy'], color='orange', label='test')
    plt.show()


# summarize model performance
def summarize_performance(scores):
    print('Accuracy: mean=%.3f std=%.3f, n=%d' % (mean(scores) * 100, std(scores) * 100, len(scores)))
    plt.boxplot(scores)
    plt.show()
