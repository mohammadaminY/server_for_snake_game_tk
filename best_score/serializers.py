from rest_framework import serializers
from score.models import BestScore


class BestScoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestScore
        fields = '__all__'
