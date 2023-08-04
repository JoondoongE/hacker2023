from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm, LoginForm

# Create your views here.
# html의 form태그로 회원가입을 하기 위한 회원가입 함수
# def register(request):
#     if request.method =='GET':
#         return render(request, 'account/register.html')
    
#     elif request.method =='POST':
#         user_id = request.POST.get('id', '')
#         user_pw = request.POST.get('pw', '')
#         user_pw_confirm = request.POST.get('pw-confirm', '')
#         user_name = request.POST.get('name', '')
#         user_email = request.POST.get('email', '')

#         if(user_id or user_pw or user_pw_confirm or user_name or user_email) == '':
#             return redirect('/account/register')
#         elif user_pw != user_pw_confirm:
#             return redirect('/account/register')
#         else:
#             user = User(
#                 user_id=user_id,
#                 user_pw=user_pw,
#                 user_name=user_name,
#                 user_email=user_email
#             )
#             user.save()
#         return redirect('/')

#forms.py를 이용한 회원가입 로직
def register(request):
    register_form = RegisterForm()
    context = {'forms':register_form}

    if request.method =='GET':
        return render(request, 'account/register2.html', context)
    
    elif request.method =='POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = User(
                user_id = register_form.user_id,
                user_pw = register_form.user_pw,
                user_name = register_form.user_name,
                user_email = register_form.user_email,
                user_phone = register_form.user_phone,
                user_gender = register_form.user_gender
            )
            user.save()
            return redirect('/')
        else:
            context['forms'] = register_form
            if register_form.errors:
                for value in register_form.errors.values():
                    context['error'] = value
        return render(request, 'account/register2.html', context)
    

#로그인 
def login(request):
    loginform = LoginForm()
    context ={'forms':loginform}

    if request.method =='GET':
        return render(request, 'account/login.html', context)
    
    elif request.method == 'POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            request.session['login_session']= loginform.login_session
            request.session.set_expiry(0)
            return redirect('/')
        else:
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request, 'account/login.html',context)
    
#로그아웃
def logout(request):
    request.session.flush()
    return redirect('/')

# def naver(request):
#     return render(request,'account/new_main.html')
