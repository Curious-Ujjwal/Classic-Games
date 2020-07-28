from django.shortcuts import render

# Create your views here.
def play_chess(request):
    cells = [(i,j) for i in range(8) for j in range(8)]
    cell_sum = [i+j for i in range(8) for j in range(8)]
    return render(request,'chess/chess.html',{'cell':cells,'cell_sum':cell_sum})


def index(request):
    return render(request,'index.html')
