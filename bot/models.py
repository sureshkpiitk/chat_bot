from django.db import models

# Create your models here.


class SearchHistory(models.Model):
    key = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'bot'
