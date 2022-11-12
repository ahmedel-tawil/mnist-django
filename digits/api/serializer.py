from rest_framework import serializers
from ..models import Digits
import base64
import uuid
from django.core.files.base import ContentFile

#
# class ImageField64Base(serializers.ImageField):
#     def to_internal_value(self, data):
#         _format, str_img = data.split(';base64')
#         decoded_file = base64.b64decode(str_img)
#         filename = f"{str(uuid.uuid4())[:10]}.png"
#         data = ContentFile(decoded_file, name=filename)
#         return super().to_internal_value(data)


class DigitSerializer(serializers.ModelSerializer):
   # image = ImageField64Base()
    class Meta:
        model = Digits
        fields = ('id', 'image', 'result')
