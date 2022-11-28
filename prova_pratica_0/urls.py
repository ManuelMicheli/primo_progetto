from django.urls import path
from .views import index1,media,somma
app_name="prova_pratica_0"
urlpatterns=[
    path('index1/',index1,name="index1"),
    path('somma/',somma,name="somma"),
    path('media/',media,name="media"),
]