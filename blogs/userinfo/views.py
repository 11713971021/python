from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from utils.check_code import create_validate_code
from io import BytesIO
from time import sleep
# Create your views here.


def login_views(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:

        users = User()
        users.user = request.POST.get('user')
        users.password = request.POST.get('password')
        a = User.objects.filter(user=users.user,
                                password=users.password)
        # 在ＰＯＳＴ提交中取出ｃｏｄｅ
        code = request.POST.get('code')
        # 验证吗　的唯一性　从ｓｅｓｓｉｏｎ中去处　cheng_code
        cheng_code = request.session.get('cheng_code', None)

        if a and code == cheng_code:
            # 在session中存入　两个session
            request.session['is_login'] = True
            request.session['names'] = users.user
            sleep(1)
            return redirect('/index/')

        elif a and code != cheng_code:
            return render(request, 'login.html', {'code_error': '验证码错误'})
        else:
            return render(request, 'login.html', {'log': '密码错误'})


def register_views(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        users = User()
        user = request.POST.get('user')
        print(user)
        password = request.POST.get('password')
        print(password)
        password1 = request.POST.get('password1')
        print(password1)
        email = request.POST.get('qq')
        # 判断用户是否存在，保证帐号的唯一性
        a = User.objects.filter(user=user)
        if len(a) > 0:
            return render(request, 'register.html', {'msg': 'user exist'})

          # 在ＰＯＳＴ提交中取出ｃｏｄｅ
        code = request.POST.get('code')
        # 验证吗　的唯一性　从ｓｅｓｓｉｏｎ中去处　cheng_code
        cheng_code = request.session.get('cheng_code', None)

        if password != password1 and code == cheng_code:
            return render(request, 'register.html', {'error': '输入的密码不一致'})

        elif password == password1 and code != cheng_code:
            return render(request, 'register.html', {'code_error': '验证码错误'})

        elif password != password1 and code != cheng_code:
            return render(request, 'register.html')

        else:
            User.objects.create(user=user,
                                password=password,
                                email=email)
            return redirect('/login/')


def imgs_views(request):
    # 存入　内存中
    f = BytesIO()
    img, code = create_validate_code()
    print(code)
    # 将的到的字符传　验证字符放入session中
    request.session['cheng_code'] = code
    img.save(f, 'PNG')
    return HttpResponse(f.getvalue())
