from django.contrib.auth import get_user_model
from django.db import models


class SearchWord(models.Model):
    word = models.CharField(max_length=512)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

