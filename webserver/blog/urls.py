from django.urls import path, re_path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/', PostListView.as_view(), name='post_list'),
    re_path(r'^post/(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post_detail'),
    path('archive/', PostArchiveIndexView.as_view(), name='post_archive'),
    path('<int:year>/', PostYearArchiveView.as_view(), name='post_year_archive'),
    path('<int:year>/<str:month>/', PostMonthArchiveView.as_view(), name='post_month_archive'),
    path('<int:year>/<str:month>/<int:day>/', PostDayArchiveView.as_view(), name='post_day_archive'),
    path('today/', PostTodayArchiveView.as_view(), name='post_today_archive'),
    path('tag/', TagTemplateView.as_view(), name='tag_cloud'),
    re_path(r'^tag/(?P<tag>[^/]+(?u))/$', PostTaggedObjectListView.as_view(), name='tagged_object_list'),
    path('search/', SearchFormView.as_view(), name='search'),
]
