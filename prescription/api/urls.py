from django.urls import path
from .views import PrescriptionGET, PrescriptionSAVE, Prescriptiondetailviews
from .views import prescription_get, prescription_save

urlpatterns = [
    # path('prescription/save', PrescriptionSAVE.as_view()),
    # path('prescription/get', PrescriptionGET.as_view()),
    path('<int:id>', Prescriptiondetailviews.as_view()),
    # path('prescription', prescription, name='home'),
    path('get', prescription_get, name='prescription_get'),
    path('save', prescription_save, name='prescription_save')

]