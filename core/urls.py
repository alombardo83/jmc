from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('media/<path:path>', views.media_access, name='media_access'),
]
