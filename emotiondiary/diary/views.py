from django.views.generic import ListView, CreateView
from allauth.socialaccount.models import SocialAccount
from diary.forms import MessageForm
from diary.models import Message
from django.shortcuts import redirect
from members.views import SocialAccountDetailMixin

import json


class DiaryView(SocialAccountDetailMixin, ListView):
    template_name = "diary/diary.html"
    model = Message

    def dispatch(self, request, *args, **kwargs):
        user = SocialAccount.objects.filter(user_id=self.request.user.id, provider='facebook')
        messages_object = Message.objects.filter(user=user)
        if (messages_object.count() == 0):
            return redirect('/diary/create/')

        return super(DiaryView, self).dispatch(request, *args, **kwargs)

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

    def form_valid(self, form):
        user = SocialAccount.objects.filter(user_id=self.request.user.id, provider='facebook')
        self.object = form.save(commit=False)
        self.object.user = user[0]
        self.object.save()

        return super(DiaryCreateView, self).form_valid(form)
