from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

fr = open('../info.txt', 'r')
lines = fr.readlines()
info_name = lines[0].rstrip('\n')
info_client_id = lines[1].rstrip('\n')
info_secret = lines[2].rstrip('\n')
fr.close()

example_site = Site.objects.all()[0]
facebook_site = Site.objects.create(domain='facebook.com', name='facebook.com')

social_app = SocialApp.objects.create(
    provider='facebook',
    name=info_name,
    client_id=info_client_id,
    secret=info_secret)
social_app.save()

social_app.sites.add(example_site)
social_app.sites.add(facebook_site)
