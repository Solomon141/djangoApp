from django.urls import path
from .views import Prescriptiondetailviews
from .views import prescription_get, prescription_save

urlpatterns = [
    path('<int:id>', Prescriptiondetailviews.as_view()),
    path('get', prescription_get, name='prescription_get'),
    path('save', prescription_save, name='prescription_save')

]