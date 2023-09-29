from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('mainpage',include("app.urls")),
    path('admin/', admin.site.urls),
    path('',include("app.urls")),
    
    
]
