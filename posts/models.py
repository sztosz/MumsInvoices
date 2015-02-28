from django.db import models

from authentication.models import Account


class Post(models.Model):
    author = models.ForeignKey(Account)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    upadated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{}'.format(self.content)
