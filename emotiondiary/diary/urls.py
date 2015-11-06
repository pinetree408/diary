from django.conf.urls import url
from diary import views

urlpatterns = [
    url(r'^$', views.DiaryView.as_view(), name='index'),
    url(r'^create/$', views.DiaryCreateView.as_view(), name='create'),
]
