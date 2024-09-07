from django.urls import path

from .views import PredictView, index

urlpatterns = [
    path('api/predict/', PredictView.as_view(), name='predict'), 
    path('', index, name='index')
]