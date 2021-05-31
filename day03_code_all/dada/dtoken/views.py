import json
import time

from django.http import JsonResponse
from django.shortcuts import render
from user.models import UserProfile
from django.conf import settings

# Create your views here.
def tokens(request):

    #http://127.0.0.1:7000/dadashop/templates/login.html
    #10200-10299

    #请确认前端页面请求地址是否正常
    #sudo su
    #cd /var/www/html/dadashop/templates/
    #vim login.html
    #103行  url: baseUrl+'/v1/tokens',
    #修改完后，记得浏览器刷新页面
    if request.method != 'POST':
        result = {'code':10200, 'error':'Please use POST'}
        return JsonResponse(result)
    #{"username":"123123","password":"12312123","cart":null}
    data = request.body
    json_obj = json.loads(data)
    #校验密码
    username = json_obj.get('username')
    password = json_obj.get('password')
    #TODO 检查一下 username or password是否获取到
    try:
        user = UserProfile.objects.get(username=username)
    except Exception as e:
        result = {'code':10201, 'error':'The username or password is wrong ~'}
        return JsonResponse(result)

    import hashlib
    m = hashlib.md5()
    m.update(password.encode())

    if m.hexdigest() != user.password:
        result = {'code':10202, 'error':'The username or password is wrong ~~'}
        return JsonResponse(result)
    #签发token
    token = make_token(username)
    #生成token
    return JsonResponse({'code':200, 'username':username,'data':{'token':token.decode()}})



def make_token(username, expire=3600 * 24):

    import jwt
    key = settings.DADA_TOKEN_KEY
    now = time.time()
    payload = {'username': username, 'exp': int(now + expire)}
    return jwt.encode(payload, key, algorithm='HS256')
























