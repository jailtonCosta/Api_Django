from django.urls import path

from .views import CursoAPView, AvaliacaoAPView

urlpatterns = [
    path('cursos/', CursoAPView.as_view(), name='cursos'),

]