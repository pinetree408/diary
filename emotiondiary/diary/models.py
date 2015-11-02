from django.db import models
from allauth.socialaccount.models import SocialAccount

import json


class Message(models.Model):

    user = models.ForeignKey(SocialAccount)
    text = models.TextField(u"text")
    created_at = models.DateTimeField(u"created at", auto_now_add=True)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return "%s" % (self.text,)

    def as_dict(self):
        data = {
            'id': self.pk,
            'created_at': self.created_at.strftime('%Y-%m-%d'),
            'text': self.text
        }
        return json.dumps(data)
