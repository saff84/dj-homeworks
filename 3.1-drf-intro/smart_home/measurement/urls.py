from django.urls import path

from .views import ViewSensors, SingleViewSensors, CreateMeasurement

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', ViewSensors.as_view()),
    path('sensors/<int:pk>/', SingleViewSensors.as_view()),
    path('measur/', CreateMeasurement.as_view()),
]
