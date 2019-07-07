from django.contrib import admin
from django.urls import path, include
from .views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', main)
]
