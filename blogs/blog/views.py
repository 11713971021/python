from django.shortcuts import render, redirect
from django.http import HttpResponse
from userinfo.models import *
from .models import *
from django.db import DatabaseError
import logging

# 分页
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index_views(request):
    if request.session.get('is_login', None):
        name = request.session.get('names', None)
        blogs_obj = User.objects.filter(user=name)[0]
        blogs = blogs_obj.blogs_set.all()

        return render(request, 'index.html', locals())

        # time = User.objects.filter(time)
        # print(time)
        # 反响查询
        # # 查询到 session 里面的ＵＳＥＲ　id

    else:
        return redirect('/login/')


# 删除session
def delete_views(request):
    del request.session['is_login']
    del request.session['names']
    return redirect('/login/')


def write_views(request):
    if request.method == 'GET':
        name_write = request.session.get('names', None)

        return render(request, 'write_.html', locals())
    else:

        # blog1 = Blogs()
        title = request.POST.get('title')
        body = request.POST.get('body')
        times = request.POST.get('times')
        name_write = request.session.get('names', None)
        blogs_ob = User.objects.filter(user=name_write)[0]
        if title and body and times:
            try:
                Blogs.objects.create(title=title,
                                     body=body,
                                     times=times,
                                     bu=blogs_ob)
            except DatabaseError as e:
                logging.warning(e)
                return render(request, 'write_.html')
            return redirect('/index/')
        return render(request, 'write_.html')


def page_views(request):
    if request.session.get('is_login', None):
        ids = request.POST.get('ids')
        blog = Blogs.objects.get(id=ids)
        print(type(blog))

        
        return render(request, 'page.html', locals())

    # user_blogs = []
    # # 获取session names
    # name = request.session.get('names', None)
    # blogs_ob = User.objects.filter(user=name)[0]
    # blogs = blogs_ob.blogs_set.all()

    # print(type(blogs))
    # for blog in blogs:
    #     print(blog.id)
    #     user_blogs.append(blog.id)
    # # 设置一次显示十个

    # page_count = 10

    # page = request.GET.get('p')
    # page = int(page)
    # start = (page-1) * page_count
    # end = page * page_count
    # data = user_blogs[start:end]
    # if page <= 1:
    #     page = 1

    # shang_page = page - 1
    # next_page = page + 1
    # return render(request, 'page.html', {'user_blogs': data,
    #                                      'shang_page': shang_page,
    #                                      'next_page': next_page})
    pass
