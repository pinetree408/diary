from django.views.generic import CreateView
from allauth.socialaccount.models import SocialAccount
from diary.forms import MessageForm
from diary.models import Message

import json

class DiaryView(CreateView):
	template_name = "diary/diary.html"
	form_class = MessageForm
	success_url = '/diary'
	model = Message

	def form_valid(self, form):
		user = SocialAccount.objects.filter(user_id=self.request.user.id, provider='facebook')
		self.object = form.save(commit=False)
		self.object.user = user[0]
		self.object.save();

		return super(DiaryView, self).form_valid(form)

	def get_context_data(self,  **kwargs):

		context = super(DiaryView, self).get_context_data(**kwargs)
		user = SocialAccount.objects.filter(user_id=self.request.user.id, provider='facebook')
		messages = Message.objects.filter(user=user)		
		messages = list(map(lambda message: message.as_dict(), messages))
		context['messages'] = messages

		return context
