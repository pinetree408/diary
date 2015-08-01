from django.shortcuts import render
#Social Account
from allauth.socialaccount.models import SocialAccount

def index(request):

        user_profile = ''
	if request.user.is_authenticated():
		user = SocialAccount.objects.filter(user_id=request.user.id, provider='facebook')
		user_profile = user[0].extra_data
	context={'test': user_profile}

	return render(request, 'emotiondiary.html', context)


