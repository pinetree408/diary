from django.views.generic import ListView, CreateView, UpdateView
from allauth.socialaccount.models import SocialAccount
from diary.forms import MessageForm
from diary.models import Message
from django.shortcuts import redirect
from members.views import SocialAccountDetailMixin

import json
import datetime

class DiaryView(SocialAccountDetailMixin, ListView):
    template_name = "diary/diary.html"
    model = Message

    def get_context_data(self,  **kwargs):
        context = super(DiaryView, self).get_context_data(**kwargs)
        user = SocialAccount.objects.filter(user_id=self.request.user.id, provider='facebook')
        messages_object = Message.objects.filter(user=user)
        messages = list(map(lambda message: message.as_dict(), messages_object))

        context['messages'] = messages

        return context


class DiaryCreateView(SocialAccountDetailMixin, CreateView):
    template_name = "diary/diary-create.html"
    form_class = MessageForm
    success_url = '/diary/'

    def get_context_data(self,  **kwargs):
        context = super(DiaryCreateView, self).get_context_data(**kwargs)
        context['year'] = self.kwargs['year']
        context['month'] = self.kwargs['month']
        context['date'] = self.kwargs['date']

        return context

    def form_valid(self, form):
        user = SocialAccount.objects.filter(user_id=self.request.user.id, provider='facebook')
        year = int(self.kwargs['year'])
        month = int(self.kwargs['month'])
        date = int(self.kwargs['date'])
        self.object = form.save(commit=False)
        self.object.user = user[0]
        self.object.created_at = datetime.datetime(year, month, date)
        self.object.save()

        return super(DiaryCreateView, self).form_valid(form)


class DiaryUpdateView(SocialAccountDetailMixin, UpdateView):
    template_name = "diary/diary-update.html"
    model = Message
    form_class = MessageForm
    success_url = '/diary/'

    def get_object(self, queryset=None):
        obj = self.model.objects.get(id=self.kwargs['id'])
        return obj

    def get_context_data(self,  **kwargs):
        context = super(DiaryUpdateView, self).get_context_data(**kwargs)
        context['id'] = self.kwargs['id']

        return context

    def form_valid(self, form):
	self.object = form.save(commit=False)
        self.object.save()

        return super(DiaryUpdateView, self).form_valid(form)
