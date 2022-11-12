
from rest_framework import viewsets
from ..models import Digits
from .serializer import DigitSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

class DigitViewSet(APIView):


    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        digits = Digits.objects.all()
        serializer = DigitSerializer(digits, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        digit_serializer = DigitSerializer(data=request.data)
        if digit_serializer.is_valid():
            digit_serializer.save()
            return Response(digit_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', digit_serializer.errors)
            return Response(digit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
