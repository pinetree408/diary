from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

example_site = Site.objects.all()[0]
facebook_site = Site.objects.create(domain='facebook.com', name='facebook.com')

social_app = SocialApp.objects.create(
    provider='facebook',
    name='',
    client_id='',
    secret='')

social_app.save()
social_app.sites.add(example_site)
social_app.sites.add(facebook_site)
