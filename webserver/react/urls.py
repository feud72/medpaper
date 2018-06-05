from django.urls import path

from .views import ReactView


app_name = 'react'

urlpatterns = [
        path('', ReactView.as_view(), name = 'index'),
        ]
