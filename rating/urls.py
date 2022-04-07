from . import views
from django.urls import path

urlpatterns = [
    path('', views.RatingList.as_view(), name='rating_list'),
    path('add', views.RatingAdd.as_view(), name='rating_add'),
]
