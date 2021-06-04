from django.db import models


class SearchWord(models.Model):
    word = models.CharField(max_length=512, primary_key=True)

