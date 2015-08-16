#Class based view
from members.views import SocialAccountDetailMixin
from django.views.generic import TemplateView

class IndexView(SocialAccountDetailMixin, TemplateView):
	template_name = "app/emotiondiary.html"
