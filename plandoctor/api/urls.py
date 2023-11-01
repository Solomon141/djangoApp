from django.urls import path
from .views import PlanDoctorviews, PlanDoctordetailviews, PlanGetDoctorviews

urlpatterns = [
    path('plandoctorget', PlanGetDoctorviews.as_view()),
    path('plandoctor', PlanDoctorviews.as_view()),
    path('plandoctor/<int:id>', PlanDoctordetailviews.as_view()),
]
