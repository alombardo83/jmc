from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('gallery/', include('photologue.urls')),
    path('rating/', include('rating.urls')),
    path('', include('core.urls')),
]

handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'
handler403 = 'core.views.handler403'
