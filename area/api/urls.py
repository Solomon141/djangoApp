from django.urls import path
from .views import Areaviews, Areadetailviews
urlpatterns = [
    path('area', Areaviews.as_view()),
    path('area/<int:id>', Areadetailviews.as_view()),
]