#Social Account
from allauth.socialaccount.models import SocialAccount

class SocialAccountDetailMixin(object):

	def get_context_data(self,  **kwargs):
		user_profile = ''
		request = self.request
		if request.user.is_authenticated():
			user = SocialAccount.objects.filter(user_id=request.user.id, provider='facebook')
			user_profile = user[0].extra_data

		
		context = super(SocialAccountDetailMixin, self).get_context_data(**kwargs)
		context['profile'] = user_profile
		print user_profile
		context['profile_image'] = "http://graph.facebook.com/{}/picture?width=40&height=40".format(user_profile['id'])
		return context

