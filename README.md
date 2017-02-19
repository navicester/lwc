# Index


# 02 Start First Django Project
本章内容包括
- Django的安装
- 创建django项目
- 本地服务器的启动
- 初始化数据库

## 安装django
``` dos
pip install django=1.5.5
```

## 创建django项目
``` dos
django-admin.py startproject lwc
```

## 启动本地服务器
``` dos
python manage.py runserver
```
127.0.0.1:8000 第一个django项目

## 初始化数据库
创建表
``` dos
python mange.py syncdb
```
创建表和超级用户
``` dos
python mange.py createsuperuser
```

# 03 First View using a Function Based View
基本的view功能包括
- 创建url
- 创建view

在*url.py*添加新的url
``` python
urlpatterns = patterns('',
    # Examples:
    url(r'^$', lwc.views.home', name='home'),
)
```

创建*views.py*
``` python
from django.shortcuts import render
def home():
    context = {}
    template = "home.html"
    return render(request, template, context)
```

# 04 Settings Setup Django Main Configuration
Django的主要配置
- 模板
- 调试开关

## 模板
创建lwc/templates 和 lwc/templates/home.html

## 配置*settings.py*
``` python
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR,"templates")
```

## 调试开关
DEBUG
TEMPLATE_DEBUG

# 05 Implement Bootstrap Front End Framework to Django
本章将介绍如何在django中使用bootstraps

Step1 拷贝下面代码

http://getbootstrap.com/examples/jumbotron/

step2 网络相对地址转为绝对链接或者本地链接
``` html
    <link rel="icon" href="../../favicon.ico">
    <link rel="icon" href="http://getbootstrap.com/favicon.ico">

    <!-- Bootstrap core CSS -->
    <link href="../../dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">

    href="../../dist/css/bootstrap.min.css" = http://getbootstrap.com/examples/jumbotron/../../dist/css/bootstrap.min.css

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="../../assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">
    <link href="http://getbootstrap.com/assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="jumbotron.css" rel="stylesheet">
    <link href="http://getbootstrap.com/examples/jumbotron/jumbotron.css" rel="stylesheet">

    <script src="../../assets/js/ie-emulation-modes-warning.js"></script>
    <script src="http://getbootstrap.com/assets/js/ie-emulation-modes-warning.js"></script>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="http://code.jquery.com/jquery-latest.js"></script>

    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script>window.jQuery || document.write('<script src=" http://getbootstrap.com/assets/js/vendor/jquery.min.js"><\/script>')</script>

    <script src="../../dist/js/bootstrap.min.js"></script>
    <script src="http://getbootstrap.com/dist/js/bootstrap.min.js"></script>

    <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
    <script src="http://getbootstrap.com/assets/js/ie10-viewport-bug-workaround.js"></script>
```

# 06 Start a Django
本节将介绍如果创建一个django应用，包括
- model & db
- admin
- form

## 创建application
``` dos
python manage.py startapp joins
```

## 创建model
*joins/models.py*
``` python
# Create your models here.
class Join(models.Model):
	email =  models.EmailField()
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return "%s " %(self.email)
```

## 生成数据表
``` dos
python manage.py syncdb
```

将会创建joins_join表

需执行这个命令，否则user auth里找不到对应的model

## 创建admin接口
*Joins\admin.py*
``` python
from django.contrib import admin
from .models import Join

class JoinAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'timestamp', 'updated']
	class Meta:
		model = Join

admin.site.register(Join, JoinAdmin)
```

https://docs.djangoproject.com/en/1.6/ref/models/fields/ 已失效

https://docs.djangoproject.com/en/1.10/ref/models/fields/


# 07 Using Django Forms
form的修改包括
- 创建新的form文件，并定义form
- View中对form进行处理，包括
 - Get
 - Post
- 模板中添加form

新建form文件*lwc/forms.py*，并定义form
``` python
from django import forms
from .models import Join

class EmailForm(forms.Form):
	name = forms.CharField(required = False)
	email = forms.EmailField()

class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
```

添加对form的处理
- nonModel Form
- ModelForm

*joins/views.py*
``` python
def home(request):
	form = EmailForm(request.POST or None)
	if form.is_valid():
		email =  form.cleaned_data['email']
		new_join, created = Joins.objects.get_or_create(email=email)
		print new_join, created

	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email = email)

	context = {"form":form}
	template = "home.html"
	return render(request, template, context)
```

模板中添加form

*templates/home.html*
``` html
{% extends "base.html" %}

{% block content %}
<h1> Welcome Home! </h1>

<form method="POST" action=""> {% csrf_token %}
    <input type="email" name="email" placeholder="Your email..." />
	{{form.as_p}}
	<input type="submit" value="join" class="btn" />
</form>
{% endblock %}
```

method 这儿可以是GET或者POST

action 是url

{% csrf_token %} 安全，防止密码泄露

form可以用non-Model form或者model form








































