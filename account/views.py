from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def signup(request):
    if request.method == 'GET':
          return render(request, 'signup.html')
    elif request.method == 'POST':
        # user_name = request.POST.get('用户名')
        # pass_word = request.POST.get('密码')
        # pass_word2 = request.POST.get('确认密码')
        user_name = request.POST['用户名']
        pass_word = request.POST['密码']
        pass_word2 = request.POST['确认密码']
        try:
            User.objects.get(username=user_name)
            return render(request, 'signup.html', {'用户名错误': '该用户已存在'})
        except User.DoesNotExist:
            if pass_word == pass_word2:
                User.objects.create_user(username=user_name, password=pass_word)
                return redirect('产品主页')
            else:
                return render(request, 'signup.html', {'密码错误': '密码不一致'})

def login(request):
    if request.method == 'GET':
          return render(request, 'login.html')
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        pass_word = request.POST['密码']
        user = auth.authenticate(username=user_name, password=pass_word)
        if user is None:
            return render(request, 'login.html', {'登录错误': '用户名或密码错误'})
        else:
            auth.login(request, user)
            return redirect('产品主页')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('产品主页')
