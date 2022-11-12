from CNN.graphs import summarize_diagnostics, summarize_performance
from CNN.load_data import load_dataset
from cnn_model import model_cnn
from CNN.model_fit import evaluate_model
from CNN.normalization import normalization


def save_model():
    # load dataset
    trainX, trainY, testX, testY = load_dataset()
    trainX, testX = normalization(trainX, testX)
    model = model_cnn()
    # fit model
    model.fit(trainX, trainY, epochs=10, batch_size=32, verbose=0)
    # save model
    model.save('mnist_model.h5')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     save_model()
