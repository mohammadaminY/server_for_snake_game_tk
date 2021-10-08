from django.db import models
from django.contrib.auth.models import User


class BestScore(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    best_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
