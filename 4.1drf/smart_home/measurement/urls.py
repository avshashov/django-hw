from django.urls import path

from measurement.views import SensorView, SensorsView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
