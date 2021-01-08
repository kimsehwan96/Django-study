from django.core import paginator
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .models import Board
from .forms import BoardForm
from user.models import User
from tag.models import Tag
# Create your views here.

def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk) #디테일에 해당하는 글
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')
    context = {
        'board' : board
    }
    return render(request, 'board_detail.html', context)

def board_write(request):
    if not request.session.get('user'): #세션 정보에 User 가 없으면
        return redirect('/user/login') #login 페이지로 리다이렉트
    
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id) 

            tags = form.cleaned_data['tags'].split(',')
            board = Board()
            board.title = form.cleaned_data['title'] #cleaned_data는 BoardForm 클래스가 상속받은 베이스 클래스에 있다.
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()

            for tag in tags:
                if not tag:
                    continue

                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)




            return redirect('/board/list')
    else:
        form = BoardForm()

    form = BoardForm()
    context = {'form' : form}
    return render(request, 'board_write.html', context) #이렇게 context라고 명시해서 넘기는게 편한듯


def board_list(request):
    #클래스.objects().all() <- 모든것을 가져옴 
    all_boards = Board.objects.all().order_by('-id') #-id는 게시글 id의 역순이라는 의미
    page = request.GET.get('p', 1)
    paginator = Paginator(all_boards, 2) #페이지네이터 클래스 인스턴스 생성

    boards = paginator.get_page(page) #페이지네이터 인스턴스의 메서드중 get_page 사용

    context = {
        'boards' : boards
    }
    return render(request, 'board_list.html', context)