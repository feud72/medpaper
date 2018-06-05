from django.urls import path

from .views import IndexView, get_name

app_name = 'form'

urlpatterns = [
        path('', get_name),
        ]
