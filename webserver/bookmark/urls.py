from django.urls import path

from .views import BookmarkListView, BookmarkDetailView

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkListView.as_view(), name='index'),
    path('<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
]
