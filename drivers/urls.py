from django.urls import path
from drivers.views import *

urlpatterns = [
    path('createorder/', OrderCreateAPIView.as_view(), name='drivers_createorder'),
    path('recommendationlist/', RecommendationListAPIView.as_view(), name='recommendation_list'),
    path('detail/<int:pk>/', DriverDetailAPIView.as_view(), name='drivers_detail'),
    path('riding/<int:id>/', RidingView.as_view(), name='drivers_status_riding'),
]