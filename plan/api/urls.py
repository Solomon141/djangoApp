from django.urls import path
from .views import PlanList, PlanSave, Plandetailviews, PlanMonthly

urlpatterns = [
    path('between/<int:pyear>/<int:pmonth>', PlanMonthly.as_view()),
    # path('plan', Planviews.as_view()),
    path('plan', PlanList.as_view()),
    path('plansave', PlanSave.as_view()),
    path('plan/<int:id>', Plandetailviews.as_view()),
]