from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from diary import views

urlpatterns = [
    url(r'^$', views.DiaryView.as_view(), name='index'),
    url(r'^create/$', login_required(views.DiaryCreateView.as_view()), name='create'),
]
