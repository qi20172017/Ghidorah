from django.db import models

# Create your models here.
class UserProfile(models.Model):

    username = models.CharField(max_length=11, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=32, verbose_name='密码')
    email = models.EmailField()
    phone = models.CharField(max_length=11, verbose_name='手机好')
    isActive = models.BooleanField(default=False, verbose_name='是否激活')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'user_profile'

    def __str__(self):
        return 'username is %s'%(self.username)

#python3 manage.py makemigrations
#python3 manage.py migrate

#POST  /v1/users






