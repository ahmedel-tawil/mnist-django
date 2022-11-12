# evaluate a model using k-fold cross-validation
from sklearn.model_selection import KFold
from .cnn_model import model_cnn


def evaluate_model(data_x, data_y, n_folds=5):
    scores, histories = list(), list()
    # prepare cross validation
    kfold = KFold(n_folds, shuffle=True, random_state=1)
    # enumerate splits
    for train_ix, test_ix in kfold.split(data_x):
        # define model
        model = model_cnn()
        # select rows for train and test
        trainX, trainY, testX, testY = data_x[train_ix], data_y[train_ix], data_x[test_ix], data_y[test_ix]
        # fit model
        history = model.fit(trainX, trainY, epochs=10, batch_size=32, validation_data=(testX, testY), verbose=0)
        # evaluate model
        _, acc = model.evaluate(testX, testY, verbose=0)
        print('> %.3f' % (acc * 100.0))
        # stores scores
        scores.append(acc)
        histories.append(history)

    return scores, histories
