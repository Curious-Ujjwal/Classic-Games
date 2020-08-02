from django.shortcuts import render

# Create your views here.
def solve_sudoku(request):
    sudoku_cells = [str(i) for i in range(9)]
    dict = {'sudoku_cells':sudoku_cells}
    return render(request,'sudoku_solver/sudoku_solver.html',dict)
