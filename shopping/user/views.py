from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ResgisterForm, LoginForm
# Create your views here.

def index(request):
    # print(request.session.items()) # for debugging.
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

    def form_valid(self, form): #이 메서드는 유효성 검사가 끝났을때, 모든 데이터가 정상적일때 동작함
        self.request.session['user'] = form.email
        return super().form_valid(form)
    #내가 조진 삽질 -> form_vaild가 아니라 form_valid임