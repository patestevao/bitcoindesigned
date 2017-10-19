from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Infographic, Tag


class HomeListView(ListView):
    model = Infographic
    template_name = 'public/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class InfographicDetailView(DetailView):
    model = Infographic
    slug_field = 'slug'
    template_name = 'public/infographic.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super(InfographicDetailView, self).get_context_data(**kwargs)
        this_infographic = Infographic.objects.filter(slug=slug).first()

        try:
            next_infographic = this_infographic.get_next_by_pub_date()
        except Infographic.DoesNotExist:
            next_infographic = None
        try:
            prev_infographic = this_infographic.get_previous_by_pub_date()
        except Infographic.DoesNotExist:
            prev_infographic = None

        context['next_infographic'] = next_infographic
        context['prev_infographic'] = prev_infographic

        return context


class TagListView(ListView):
    model = Infographic
    template_name = 'public/tag.html'

    def get_queryset(self, **kwargs):
        tag_slug = self.kwargs['slug']
        queryset = Infographic.objects.filter(tags__slug=tag_slug).all()
        if queryset:
            return queryset
        raise Http404

    def get_context_data(self, **kwargs):
        tag_slug = self.kwargs['slug']
        tag = Tag.objects.filter(slug=tag_slug).first()

        context = super(TagListView, self).get_context_data(**kwargs)
        context['tag'] = tag

        return context


def about(request):
    return render(request, 'public/about.html')
