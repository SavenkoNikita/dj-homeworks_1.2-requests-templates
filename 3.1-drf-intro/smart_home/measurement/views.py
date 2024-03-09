# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from django.forms import model_to_dict
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, \
    get_object_or_404
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


class SensorView(CreateAPIView, ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SingleSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(self, request, pk):
        sensor_found = Sensor.objects.get(id__exact=pk)
        measures = Measurement.objects.filter(id_sensor=sensor_found)
        response = model_to_dict(sensor_found)
        response['measurements'] = [model_to_dict(measure) for measure in measures]
        return Response(response)


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        post_new = Measurement.objects.create(
            id_sensor=Sensor.objects.get(id__exact=request.data['sensor']),
            temperature=request.data['temperature'],
        )
        return Response({'Measurement': model_to_dict(post_new)})
