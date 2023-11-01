from django.urls import path
from .views import Hospitalviews, Hospitaldetailviews

urlpatterns = [
    path('hospital', Hospitalviews.as_view()),
    path('hospital/<int:id>', Hospitaldetailviews.as_view()),
]