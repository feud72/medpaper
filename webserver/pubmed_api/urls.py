from django.urls import path

from .views import ApiListView

app_name = 'pubmed_api'

urlpatterns = [
        path('', ApiListView.as_view(), name='api_list'),
        ]
