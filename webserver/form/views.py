from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from .forms import NameForm

# Create your views here.

def get_name(request):
    """docstring for get_name"""
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
            form = NameForm()
            return render(request, 'form/name.html', {'form': form})


class IndexView(TemplateView):
    template_name = 'form/name.html'
