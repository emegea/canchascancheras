from django.contrib import admin
from django.urls import path, include
from web import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('chacan/', views.chacan, name='chacan'),
]
