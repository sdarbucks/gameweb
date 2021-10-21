from django.urls import path
from . import views

app_name = "pcgame"
urlpatterns = [
    # 127.0.0.1:8000/pcgame/
    path('', views.pcgame_index, name='pcgame_index'),
]
