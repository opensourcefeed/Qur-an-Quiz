from . import views
from django.urls import path

urlpatterns = [
    path('$/', views.users, name='users')
    path('$/', views.questions, name='questions')
    path('$/', views.options, name='options')
    path('$/', views.categories, name='categories')
    path('$/', views.levels, name='levels')
    path('$/', views.scores, name='scores')
    path('$/', views.attempts, name='attempts')
]