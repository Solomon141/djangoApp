from django.urls import path
from .views import PrescriptionGET, PrescriptionSAVE, Prescriptiondetailviews

urlpatterns = [
    path('prescription/save', PrescriptionSAVE.as_view()),
    path('prescription/get', PrescriptionGET.as_view()),
    path('prescription/<int:id>', Prescriptiondetailviews.as_view()),
]