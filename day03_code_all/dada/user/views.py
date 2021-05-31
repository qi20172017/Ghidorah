#file: /user/views.py
import random

from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
import json
import base64

from .models import UserProfile
from dtoken.views import make_token
from django_redis import  get_redis_connection

r = get_redis_connection()


# Create your views here.
def users(request):

    if request.method == 'POST':
        #http://127.0.0.1:7000/dadashop/templates/test_register.html
        #处理注册
        #{"uname":"123123","password":"123123123","phone":"13091463622","email":"dada@tedu.cn"}
        #此次请求前端 Content-Type: application/json
        #如果是非表单提交，request.body
        #request.POST 只针对表单提交的POST数据进行获取
        #data去出来是 字节串，小心json.loads字节串时 会报错
        data = request.body
        json_obj = json.loads(data)
        username = json_obj.get('uname')
        email = json_obj.get('email')
        phone = json_obj.get('phone')
        password = json_obj.get('password')
        #TODO 判断数据是否存在

        #检查用户名是否可用
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            #10100 - 10199 - user
            result = {'code': 10100,  'error':'The username is existed !'}
            #JsonResponse 可直接将py对象 转化成json字符串返回，且响应头中的Content-Type的值变为 application/json
            return JsonResponse(result)

        #生成哈希密码
        import hashlib
        m = hashlib.md5()
        m.update(password.encode())
        m_password = m.hexdigest()

        #创建用户-
        try:
            user = UserProfile.objects.create(username=username,email=email,phone=phone,password=m_password)
        except Exception as e:
            result = {'code':10101, 'error': 'The username is existed !!'}
            return JsonResponse(result)

        #生成token
        token = make_token(username)

        #TODO 发送激活邮件
        #初始化随机数
        random_int = random.randint(1000, 9999)
        code_str = username + '_' + str(random_int)
        code_str_bs = base64.urlsafe_b64encode(code_str.encode())
        #将随机码存储到redis里 可以存储1-3天
        #redis?
        r.set('email_active_%s'%(username), str(random_int))
        active_url = 'http://127.0.0.1:7000/dadashop/templates/active.html?code=%s'%(code_str_bs.decode())
        #发邮件
        send_active_email(email,active_url)

        return JsonResponse({'code':200,'username':username, 'data':{'token':token.decode()}})


def send_active_email(email, code_url):

    subject = '达达商城用户激活邮件'
    html_message = '''
    <p>尊敬的用户 您好</p>
    <p>激活url为<a href='%s' target='blank'>点击激活</a></p>
    '''%(code_url)
    send_mail(subject=subject, message='', html_message=html_message,from_email='572708691@qq.com',recipient_list=[email])

def users_active(request):
    #激活用户
    if request.method != 'GET':
        result = {'code': 10102, 'error': 'Please use GET!'}
        return JsonResponse(result)
    code = request.GET.get('code')
    if not code:
        pass
    code_str = base64.urlsafe_b64decode(code.encode())
    #username_9999
    new_code_str = code_str.decode()
    username, rcode = new_code_str.split('_')

    #要获取username对应的redis中的值
    old_data = r.get('email_active_%s'%(username))
    if not old_data:
        result = {'code': 10103, 'error': 'Your code is wrong !'}
        return JsonResponse(result)
    if rcode != old_data.decode():
        result = {'code': 10104, 'error': 'Your code is wrong !'}
        return JsonResponse(result)

    user = UserProfile.objects.get(username=username)
    user.isActive = True
    user.save()

    #删除redis里面对应的数据
    r.delete('email_active_%s'%(username))
    result = {'code':200, 'data':{'msg':'ok'}}
    return JsonResponse(result)
















































