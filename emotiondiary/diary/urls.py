from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from diary import views

urlpatterns = [
    url(r'^$', login_required(views.DiaryListView.as_view()), name='index'),
    url(r'^create/(?P<year>\d+)/(?P<month>\d+)/(?P<date>\d+)/$', login_required(views.DiaryCreateView.as_view()), name='create'),
    url(r'^update/(?P<pk>\d+)/$', login_required(views.DiaryUpdateView.as_view()), name='update'),
]
