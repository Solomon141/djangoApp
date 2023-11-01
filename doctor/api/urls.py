from django.urls import path
from .views import Doctorviews, Doctordetailviews

urlpatterns = [
    path('doctor', Doctorviews.as_view()),
    path('doctor/<int:id>', Doctordetailviews.as_view()),
]