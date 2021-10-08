from django.contrib import admin
from best_score.models import BestScore


@admin.register(BestScore)
class BestScoreAdmin(admin.ModelAdmin):
    list_display = ['user', 'best_score', 'created_at']
