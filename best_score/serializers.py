from rest_framework import serializers
from best_score.models import BestScore
from django.contrib.auth.models import User


class BestScoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestScore
        fields = '__all__'
