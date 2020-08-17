
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('obtaining_points_methods/', include('points.urls')),
    path('admin/', admin.site.urls),
]
