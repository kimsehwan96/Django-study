from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm
from user.models import User
# Create your views here.

def board_detail(request, pk):
    board = Board.objects.get(pk=pk) #디테일에 해당하는 글
    context = {
        'board' : board
    }
    return render(request, 'board_detail.html', context)

def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id)
            board = Board()
            board.title = form.cleaned_data['title'] #cleaned_data는 BoardForm 클래스가 상속받은 베이스 클래스에 있다.
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()

            return redirect('/board/list')
    else:
        form = BoardForm()

    form = BoardForm()
    context = {'form' : form}
    return render(request, 'board_write.html', context) #이렇게 context라고 명시해서 넘기는게 편한듯


def board_list(request):
    #클래스.objects().all() <- 모든것을 가져옴 
    boards = Board.objects.all().order_by('-id') #-id는 게시글 id의 역순이라는 의미
    
    return render(request, 'board_list.html', {'boards' : boards })