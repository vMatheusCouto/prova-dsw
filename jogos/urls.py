from django.urls import path
from jogos import views

urlpatterns = [
    path('', views.index, name="index"),
    path('equipes/<int:id>/', views.equipe, name="equipe"),
    path('modalidades/<int:id>/', views.modalidade, name="modalidade"),
]
