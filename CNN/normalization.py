def normalization(train, test):
    # convert from integers to floats
    train_norm = train.astype('float32')
    test_norm = test.astype('float32')
    # normalize to range 0-1
    train_normalization = train_norm / 255.0
    test_normalization = test_norm / 255.0
    # return normalized images
    return train_normalization, test_normalization
