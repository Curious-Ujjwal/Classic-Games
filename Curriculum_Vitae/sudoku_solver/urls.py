from django.urls import path
from sudoku_solver import views

app_name = 'sudoku_solver'

urlpatterns = [
    path('',views.solve_sudoku,name='solve'),
]
