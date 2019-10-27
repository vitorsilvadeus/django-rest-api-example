from performance.views import PerformanceAPIView
from django.urls import path

urlpatterns = [
    path('', PerformanceAPIView.as_view(), name='performance'),
]