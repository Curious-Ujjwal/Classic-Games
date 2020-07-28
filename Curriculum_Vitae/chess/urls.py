from django.urls import path
from chess import views

app_name = 'chess'

urlpatterns = [
    path('',views.play_chess,name='game'),
]
