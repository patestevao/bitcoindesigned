from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.HomeListView.as_view(),
        name='home'
    ),
    url(
        regex=r'^about/$',
        view=views.about,
        name='about'
    ),
    url(
        regex=r'^infographics/(?P<slug>[\w-]+)/$',
        view=views.InfographicDetailView.as_view(),
        name='infographic_detail'
    ),
    url(
        regex=r'^tags/(?P<slug>[\w-]+)/$',
        view=views.TagListView.as_view(),
        name='tag'
    ),
]
