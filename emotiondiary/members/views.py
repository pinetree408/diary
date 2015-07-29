from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount

def index(request):

	print request.user.id
	user = SocialAccount.objects.filter(user_id=request.user.id, provider='facebook')

	context={'test': user[0].extra_data}

	return render(request, 'index.html', context)


