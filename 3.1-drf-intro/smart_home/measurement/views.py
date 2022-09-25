# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# @api_view(['GET'])
# def ViewSensors(request):
#     sensors = Sensor.objects.all()
#     sensors_ser = SensorSerializer(sensors, many = True)
#     return Response(sensors_ser.data)

# class ViewSensors(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         sensors_ser = SensorSerializer(sensors, many=True)
#         return Response(sensors_ser.data)
#
#     def post(self, request):
#         return Response({'status': 'OK'})

class ViewSensors(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SingleViewSensors(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class CreateMeasurement(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

