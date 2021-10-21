from django.urls import path
from . import views

app_name = "congame"
urlpatterns = [
    # 127.0.0.1:8000/congame/
    path('', views.congame_index, name='congame_index'),
]
