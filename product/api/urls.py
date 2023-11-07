from django.urls import path
from .views import badreg_get, badreg_save, Badregdetailviews

urlpatterns = [
    path('badreg/get', badreg_get, name='badreg_get'),
    path('badreg/save', badreg_save, name='badreg_get'),
    path('badreg/<int:id>', Badregdetailviews.as_view()),
]