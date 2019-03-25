from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import InfographicContent, Tag, Language


class HomeListView(ListView):
    model = InfographicContent
    template_name = 'public/home.html'

    def get_queryset(self, **kwargs):
        language_code = self.request.GET.get('lang', 'en')
        queryset = InfographicContent.objects.filter(infographic__active=True, language__code=language_code).all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        language_code = self.request.GET.get('lang', 'en')
        context["lang"] = language_code
        context['tags'] = Tag.objects.filter(infographic__active=True, infographic__infographiccontent__language__code=language_code).distinct()
        context['languages'] = Language.objects.filter(infographiccontent__infographic__active=True).distinct()
        return context


class InfographicDetailView(DetailView):
    model = InfographicContent
    slug_field = 'slug'
    template_name = 'public/infographic.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super(InfographicDetailView, self).get_context_data(**kwargs)
        this_infographic = InfographicContent.objects.filter(slug=slug).first()
        language_code = self.request.GET.get('lang', 'en')

        context['next_infographic'] = InfographicContent.objects.filter(
                infographic__active = True,
                infographic__pub_date__gt = this_infographic.infographic.pub_date,
                language__code = this_infographic.language.code
        ).first()

        context['prev_infographic'] = InfographicContent.objects.filter(
                infographic__active = True,
                infographic__pub_date__lt = this_infographic.infographic.pub_date,
                language__code = this_infographic.language.code
        ).first()

        return context


class TagListView(ListView):
    model = InfographicContent
    template_name = 'public/tag.html'

    def get_queryset(self, **kwargs):
        tag_slug = self.kwargs['slug']
        language_code = self.request.GET.get('lang', 'en')
        queryset = InfographicContent.objects.filter(
                infographic__active=True, infographic__tags__slug=tag_slug, language__code=language_code
        ).all()
        if queryset:
            return queryset
        raise Http404

    def get_context_data(self, **kwargs):
        tag_slug = self.kwargs['slug']
        tag = Tag.objects.filter(slug=tag_slug).first()

        context = super(TagListView, self).get_context_data(**kwargs)
        language_code = self.request.GET.get('lang', 'en')
        context["lang"] = language_code
        context['tag'] = tag
        context['languages'] = Language.objects.filter(
                infographiccontent__infographic__active=True,
                infographiccontent__infographic__tags=tag
        ).distinct()

        return context


def about(request):
    return render(request, 'public/about.html')

def translations(request):
    return render(request, 'public/translations.html')

def support(request):
    return render(request, 'public/support.html')
