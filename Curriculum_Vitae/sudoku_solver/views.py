from django.shortcuts import render

# Create your views here.
def solve_sudoku(request):
    return render(request,'sudoku_solver/sudoku_solver.html')
