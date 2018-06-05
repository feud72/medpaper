from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.views.generic.edit import FormView
from django.db.models import Q

from .forms import PostSearchForm
from .models import Post

from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2
    

class PostDetailView(DetailView):
    model = Post
    
    
class PostArchiveIndexView(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'
    
    
class PostYearArchiveView(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True
    
    
class PostMonthArchiveView(MonthArchiveView):
    model = Post
    date_field = 'modify_date'
    
    
class PostDayArchiveView(DayArchiveView):
    model = Post
    date_field = 'modify_date'
    
    
class PostTodayArchiveView(TodayArchiveView):
    model = Post
    date_field = 'modify_date'
    

class TagTemplateView(TemplateView):
    template_name = 'tagging/tagging_cloud.html'


class PostTaggedObjectListView(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()
        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

