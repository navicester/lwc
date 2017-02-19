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

# 08 Make changes to Django Models with South

## 安装south
``` dos
pip install south
```
## 配置setting
``` python
INSTALLED_APPS = (
    'joins',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'south'
)
```

用south来控制joins的migration
``` dos
python manage.py convert_to_south joins
```
这条命令会创建history和初始的migration

本地运行时，之前已有joins数据库，一个简单方法是直接删除joins/migrations,然后执行sync，将会从头执行
``` dos
python manage.py syncdb
```
将会创建表 south_migrationhistory, joins_join

执行修改
``` dos
python manage.py schemamigration joins –auto
```

migrate db
``` dos
python manage.py migrate joins
```

https://github.com/codingforentrepreneurs/Guides/blob/master/all/using_south_in_django.md
<pre>
1)	Install south : pip install south, add south to settings.py in INSTALLED APPS
2)	Ensure model is in sync in database
3)	Covert the model to south with : python manage.py convert_to_south appname
4)	Make changes to model (eg add new fields : ip_address = model.CharField(max_length=120
5)	Run schemamigration : python manage.py schemamigration appname  --auto
6)	Run migrate : python mange.py migrate
</pre>

# 09 Get User IP Address from Requests
获取ip包括以下几个步骤
- Join添加ip字段
- 更新join form的显示，ip这个字段并不开放给用户
- 从request.META.get里获取ip
- 在form处理时把这个ip存进join

https://github.com/codingforentrepreneurs/Guides/blob/master/all/using_south_in_django.md

*views.py*
``` python
def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWORDED_FOR")
		if x_forward:
			ip = x_forward.split(',')[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip


def home(request):
	'''
	form = EmailForm(request.POST or None)
	if form.is_valid():
		email =  form.cleaned_data['email']
		new_join, created = Joins.objects.get_or_create(email=email)
		print new_join, created
	'''

	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email = email)
		if created:
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
		
	context = {"form":form}
	template = "home.html"
	return render(request, template, context)

class Join(models.Model):
	email =  models.EmailField(unique = True)
	ip_address =  models.CharField(max_length = 120, default = 'ABC')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return "%s " %(self.email)

class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		fields = ['email',] #只显示email
```		

# 10 Create Custom Reference ID
Reference处理包括以下几个步骤
- 在join添加ref_id字段
- 从uuid里面拿出值，并置成ref_id
- 在form POST处理时把这个字段存进join

运行 `python manage.py shell`
``` dos
>>> import uuid
>>> uuid.uuid4()
```

``` python
class Join(models.Model):
	email =  models.EmailField(unique = True)
+	ref_id = models.CharField(max_length=120, default='ABC', unique=True)
	ip_address =  models.CharField(max_length = 120, default = 'ABC')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return "%s %s" %(self.email, self.ref_id)

+	class Meta:
+		unique_together = ("email", "ref_id",)

+import uuid
+def get_ref_id():
+	ref_id = str(uuid.uuid4())[:11].replace('-','').lower()
+	try:
+		id_exists = Join.objects.get(ref_id=ref_id)
+		get_ref_id()
+	except:
+		return ref_id


def home(request):
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email = email)
		if created:
+			new_join_old.ref_id = get_ref_id()
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
		
	context = {"form":form}
	template = "home.html"
	return render(request, template, context)
```

# 11 Create a Social Sharing Page to Share
创建分享页
- 添加url
- 将email字段unique去掉
- 添加分享页view
- 添加分享页template
- 添加view中重定向到分享页的处理

``` python
urlpatterns = patterns('',
    url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),
)

from django.shortcuts import render, HttpResponseRedirect
def home(request):

	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email = email)
		if created:
			new_join_old.ref_id = get_ref_id()
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
+		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))
		
	context = {"form":form}
	template = "home.html"
	return render(request, template, context)

class Join(models.Model):
-	email =  models.EmailField(unique = True)
+	email =  models.EmailField()
	friend = models.ForeignKey("self", related_name='referral', null=True, blank=True)
	ref_id = models.CharField(max_length=120, default='ABC', unique=True)
	ip_address =  models.CharField(max_length = 120, default = 'ABC')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return "%s %s" %(self.email, self.ref_id)
	
	class Meta:
		unique_together = ("email", "ref_id",)
```		
email unique改成False，否则Join的时候check不过

*joins/views.py*添加分享处理函数
``` python
def share(request, ref_id):
join_obj = Join.objects.get(ref_id=ref_id)
context = {"ref_id": join_obj.ref_id }
    template = "share.html"
    return render(request, template, context)	
```

*templates/share.html*
``` html
{% extends "base.html" %}

{% block content %}
{% include "navbar.html" %}

ref_id : {{ref_id}}

{% endblock %}
```

# 12 Use Custom Django Middleware to Track Shares
添加middleware处理分享页
- 添加middleware类
- 从middleware中获取reference值 (url中的内容)，并将这个值存入session
- 在view中将session中的值拿到，并根据这个值get到join

https://docs.djangoproject.com/en/1.10/topics/http/middleware/
``` python
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
+    'lwc.middleware.ReferMiddleware',
)
```

创建*lwc/middleware.py*
``` python
from joins.models import Join

class ReferMiddleware():
	def process_request(self, request):
		ref_id = request.GET.get("ref")
		try:
			obj = Join.objects.get(ref_id = ref_id)
		except:
			obj = None
			
		if obj:
			request.session['join_id_ref'] = obj.id
```

在home里增加对session结果的处理
``` python
def home(request):
+	try:
+		join_id = request.session['join_id_ref']
+		obj = Join.objects.get(id=join_id)
+	except:
+		obj = None	

	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email = email)
		if created:
			new_join_old.ref_id = get_ref_id()
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))
		
	context = {"form":form}
	template = "home.html"
	return render(request, template, context)
```

13 Save Reference ID with Foreign Key Model Fields
添加Friend，用reference id作为索引
- 在join model中添加friend字段
- 在view中将join object存为friend

添加friend字段
``` python
class Join(models.Model):
	email =  models.EmailField()
+	friend = models.ForeignKey("self", related_name='referral', null=True, blank=True)
	ref_id = models.CharField(max_length=120, default='ABC', unique=True)
	ip_address =  models.CharField(max_length = 120, default = 'ABC')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return "%s %s" %(self.email, self.ref_id)
	
	class Meta:
		unique_together = ("email", "ref_id",)
```

后台处理中将join对象存储为friend
``` python
def home(request):
	try:
		join_id = request.session['join_id_ref']
		obj = Join.objects.get(id=join_id)
	except:
		obj = None	

	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email = email)
		if created:
			new_join_old.ref_id = get_ref_id()
+			if not obj == None:
+				new_join_old.friend = obj
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))
		
	context = {"form":form}
	template = "home.html"
	return render(request, template, context)
```








































