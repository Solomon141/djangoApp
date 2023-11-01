from django.urls import path
from .views import PlanEntitydetailviews, PlanEntitySave 
# from .views import PlanEntityGet

urlpatterns = [
    # path('planentityget', PlanEntityGet.as_view()),
    path('planentitysave', PlanEntitySave.as_view()),
    path('planentity/<int:id>', PlanEntitydetailviews.as_view()),
]
