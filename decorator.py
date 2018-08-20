'''
django装饰器
@login_required
@login_required(login_url='/accounts/login/')
def my_view(request): 每次访问my_view 时，都会进入login_required
'''
'''
group_required('adnubs', 'seller')
'''


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)


@group_required('admins', 'seller')
def my_view(request, pk):
    pass

# django 登录访问限制＠login_required 在　setting设置
# 自定义装饰器


def my_login(func):

    def check_login(request):
        # 此步骤是检查登录状态
        if request.session.get('user_id'):
        # 如果当前有用户登录,正常跳转
            return func(request)

        else:
            # 如果没有用户登录，跳转到登录页面
            return redirect('/login')
    return check_login


# 如果在index页面，必须让他在login验证
@my_login
def index(request):
    '''主页'''
    return render(request, 'index.html', locals())