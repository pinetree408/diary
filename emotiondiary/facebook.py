from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

example_site = Site.objects.all()[0]
facebook_site = Site.objects.create(domain='facebook.com', name='facebook.com')

social_app = SocialApp.objects.create(
    provider='facebook',
    name='emotiondiary',
    client_id='1447094345617583',
    secret='54e60cc48404307a1ccbcee04bb4a04c')

social_app.save()
social_app.sites.add(example_site)
social_app.sites.add(facebook_site)
