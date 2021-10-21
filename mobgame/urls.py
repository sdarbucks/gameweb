from django.urls import path
from . import views

app_name = "mobgame"
urlpatterns = [
    # 127.0.0.1:8000/mobgame/
    path('', views.mobgame_index, name='mobgame_index'),
]
