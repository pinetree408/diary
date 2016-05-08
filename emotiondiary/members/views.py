# Social Account
from allauth.socialaccount.models import SocialAccount
# Views
from django.views.generic import TemplateView


class SocialAccountDetailMixin(object):

    def get_context_data(self,  **kwargs):
        user_profile = ''
        user_profile_image = ''
        context = super(SocialAccountDetailMixin, self).get_context_data(**kwargs)
        request = self.request
        if request.user.is_authenticated():
            user = SocialAccount.objects.filter(user_id=request.user.id, provider='facebook')
            user_profile = user[0].extra_data
            user_profile_image = "http://graph.facebook.com/{}/picture?width=40&height=40".format(user_profile['id'])

            context['profile'] = user_profile
            context['profile_image'] = user_profile_image

            return context


class IndexView(SocialAccountDetailMixin, TemplateView):
    template_name = "members/index.html"
