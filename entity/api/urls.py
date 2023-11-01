from django.urls import path
from .views import EntityList, EntityDetail

urlpatterns = [
    path("entity/", EntityList.as_view(), name="entity"),
    path("entity/<int:id>", EntityDetail.as_view(), name="entity"),
]