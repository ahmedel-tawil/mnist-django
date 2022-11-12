import os.path
import numpy as np
import tensorflow as tf
from django.conf import settings
from django.db import models
from django.urls import reverse
from keras_preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model


# Create your models here.
class Digits(models.Model):
    image = models.ImageField(upload_to='images')
    result = models.CharField(max_length=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('prediction-result', kwargs={'id': self.id})

    def __str__(self):
        return f'{self.id}'

    def get_prediction(self):
        img = load_img(self.image.path, grayscale=True, target_size=(28, 28))
        img = img_to_array(img)
        img = img.reshape(1, 28, 28, 1)
        img = img.astype('float32')
        img = img / 255
        file_mode = os.path.join(settings.BASE_DIR, 'CNN/mnist_model.h5')
        graph = tf.compat.v1.get_default_graph()
        with graph.as_default():
            model = load_model(file_mode)
            prediction = np.argmax(model.predict(img))
            print(f'classified as {prediction}')

        self.result = str(prediction)
        self.save()

        return prediction
