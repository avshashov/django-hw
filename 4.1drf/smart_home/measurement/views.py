from django.forms import model_to_dict
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor
from measurement.serializers import SensorSerializer, SensorsListSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsListSerializer


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(APIView):
    def post(self, request):
        new_measurement = Sensor.objects.get(id=request.data['sensor']).measurements.create(
            temperature=request.data['temperature'])
        return Response({'post': model_to_dict(new_measurement)})
