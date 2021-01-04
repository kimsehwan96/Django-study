from django.shortcuts import render
from .models import Board
from .forms import BoardForm
# Create your views here.

def board_write(request):
    form = BoardForm()
    context = {'form' : form}
    return render(request, 'board_write.html', context) #이렇게 context라고 명시해서 넘기는게 편한듯
    

def board_list(request):
    #클래스.objects().all() <- 모든것을 가져옴 
    boards = Board.objects.all().order_by('-id') #-id는 게시글 id의 역순이라는 의미
    
    return render(request, 'board_list.html', {'boards' : boards })