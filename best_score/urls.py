from best_score import views
from django.urls import path

app_name = 'best_score'
urlpatterns = [
    path('get-all-best-scores', views.get_all_best_score),
    path('create-best-score',views.create_best_score),
    path('set-best-score/<int:pk>', views.set_best_score)
]
