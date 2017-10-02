from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Infographic, Tag


# Create your views here.
# def home(request):
#     return render(request, 'public/home.html')

class HomeListView(ListView):
    model = Infographic
    template_name = 'public/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class InfographicDetailView(DetailView):
    model = Infographic
    template_name = 'public/infographic.html'


def about(request):
    return render(request, 'public/about.html')
