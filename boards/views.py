from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm

# Create your views here.
def index(request):
    boards = Board.objects.all()
    context = {
        'boards': boards,
    }
    return render(request, 'boards/index.html', context)


def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.auth = request.user
            form.save()
            return redirect('boards:index')
    else:
        form = BoardForm()
    context = {
        'form':form,
    }
    return render(request, 'boards/create.html', context)


def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board':board,
    }
    return render(request, 'boards/detail.html', context)


def update(request, pk):
    board = Board.objects.get(pk=pk)
    if request == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm(instance=board)
    context = {
        'board': board,
        'form': form,
    }
    return render(request, 'boards/update.html', context)


def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('boards:index')