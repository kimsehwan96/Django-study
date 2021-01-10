from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ResgisterForm, LoginForm
# Create your views here.

def index(request):
    context = {
        'email' : request.session.get('user')
    }
    return render(request, 'index.html', context)

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = ResgisterForm
    success_url = '/' #성공시 리다이렉션


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_vaild(self, form): #이 메서드는 유효성 검사가 끝났을때, 모든 데이터가 정상적일때 동작함
        self.request.session['user'] = form.email
        return super().form_vaild(form)