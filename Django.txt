just from 1 - 17 steps are important

1- create virtualenv [name_venv] for example: venv
2- activate venv

3- pip install django

4- django-admin startproject [firstproject]
5- cd firstproject
6-for test --  python manage.py runserver
7- python manage.py migrate

creaet app
8- python manage.py startapp [pages]
9- go to settings.py into [firstproject] and add [pages.apps.PagesConfig] into [INSTALLED_APPS]

10- go to [urls.py] into [firstproject] and write [from django.urls import path, include] and write into [urlpatterns] [path('',include('pages.urls')),]
																or
														       [path('pages/',include('pages.urls')),]
													
11- create [urls.py] into [pages] 

12- go to [views.py] into [pages] and write :

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('hello world ')

13- go to [urls.py] into [pages] and write :

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]

14- test the website by: [python manage.py runserver]


15 - go to [views.py] into [pages] and write: 

def about(request):
    return HttpResponse('about')

16- go to [urls.py] into [pages] and into [urlpatterns] write:

path('about', views.about, name='about'),

17- test the website by: [python manage.py runserver]

18- delete [HttpResponse] and use [render]

19- create [templates] Folder into main project folder [firstproject]
20- go to [settings.py] in [firstproject] project_folder and write:

[import os]
and write into [TEMPLATES] into [ 'DIR'=[os.path.join(BASE_DIR,'templates')] ]


21- create [index.html] into [templates] Folder
22- go to [views.py] into [pages] app and write in [def index()] :

return render(request, 'pages/index.html')
### I write [pages/index.html] directly because [templates] is define in ['settings.py'] in project folder 

23- write HTML into index.html

24- return render(request, 'pages/index.html, {'name':'ahmed'}')
in [index.html] write [ {{name}} ] to get ahmed

{{name}}  >> variable

25- when I apply filters I write (we apply filters after [ | ] ) like this:

{{name|capfirst}}


26- tags

{% tag %}
{% endtag %}

27- create file ['base.html'] in [templates] folder
{% extends 'base.html' %}

في أي صفحة تستخدم فيها الوراثة يجب أن تضع أكواد اتش تي ام إل داخل تاق بلوك:

content or any name
{% block content %}
	<html>
{% endblock content%}
يجب كتابتها بنفس الاسم في الصفحة الأب


28- create folder [parts] into [templates] 

29- write in ['base.html']

{% include 'parts/footer.html'%}

30- create [static] folder in (project folder) [firstproject]
31 - create [css] [js] [image] folders into [static] folder
32 - create [style.css] into [css] folder

33- go to [settings.py] into project_folder [firstproject]

34- down to last of line of file :
make variables:
#####
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'project/static'),
]
####

34- python manage.py collectstatic

35- write in [base.html] at top page :

{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">


36- write in [index.html]:

{% extends 'base.html' %}
{% load static %}
<!--name = {{name|default:'not found'}}-->

{% block content %}
<img src="{% static 'image/Untitled2.png' %}">
<h1>index page</h1>
{% endblock content%}


37- go to [templates/parts/navbar.html] and write:

<span><a href="{% url 'index' %}">home</a></span>
<span><a href="{% url 'about' %}">about</a></span>


38- comment system in [DTL] (Django Template language):
{% comment %}
{% endcomment %}


[[ new stage ]]
39- go to [pages/models.py] and write:

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)


40- create second app [products]:
python manage.py startapp products


41- go to [firstproject] and go to [settings.py] in [INSTALLED_APPS] : add the [products] app

'products.apps.ProductsConfig',


42- go to [products] app and create [urls.py]

43- go to [firstproject] (project_folder) go to [urls.py] and write in [urlpatterns]:

path('products', include('producs.urls')),


44- create super user (admin) by write:
python manage.py createsuperuser
#and write [Email] 	[Username] [Password]
azoozsm2@gmail.com	azooz4     azooz

45- go to [admin.py] in [products] and write:

from django.contrib import admin
from .models import Product

admin.site.register(Product)


46- go to [models.py] in [products] app and write:

class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)



47- python manage.py makemigration   لتسجيل الكلاس (المنتج) في دجانغو
48- python manage.py migrate         لتسجيل الكلاس (المنتج) في قاعدة البيانات


48- runserver for test website

49- create folder [products] in [templates] folder and create two files [products.html] [product.html] and write into togather:

{% extends 'base.html' %}

{% block content  %}

{% endblock content %}


50- go to [views.py] into [products] app and write:

from django.shortcuts import render

def product(request):
    return render(request, 'products/product.html')

def products(request):
     return render(request, 'products/products.html')



51- go to [urls.py] into [products] app and write:

from django.urls import path
from . import views

urlpatterns = [
    path('product',views.product, name='product'),
    path('',views.products, name='products'),
]



52- go to [views.py] into [products] app and append:
 
from django.shortcuts import render
from .models import Product


def product(request):
    return render(request, 'products/product.html')

def products(request):
     return render(request, 'products/products.html', { 'pro': Product.objects.all() } )



53- go to [products.html] into [templates/products] and write:

{% extends 'base.html' %}

{% block content  %}

{% for x in pro %}
    <h1>{{x.name}}</h1>
    <h1>{{x.content}}</h1>
    <h1>{{x.price}}</h1>

{% endfor %}

{% endblock content %}


54- go to [models.py] into [products] and write:

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'name'
### or
class Meta:
        ordering = ['name']
class Meta:
        ordering = ['price'] ### or [-price] لعكس ترتيب السعر 
###



55- go to [models.py] into [products] and append:

واحدة تظهر في الأدمن بانل وواحدة تتسجل في قاعدة البيانات س

x = [
        ('mobiles','mobiles'),
        ('computers','computers'),
    ]


category = models.CharField(max_length=50, null=True, blank=True, choices=x)


56- go to [views.py] into [products] app and write :

from django.shortcuts import render
from .models import Product


def product(request):
    return render(request, 'products/product.html')

def products(request):
    pro = Product.objects.all()
    x = { 'pro': str(pro.count()) }
    return render(request, 'products/products.html',  x)



57- go to [settings.py] into [firstproject]  and  append :   (for activate [media])

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'


58- go to [urls.py] into [firstproject] and write:

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('products/', include('products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 


59- When we want to show <img> in browser we use:

<img src="{{x.image.url}}" />

تظهر الصور بعد إضافة أوبجكت جديد بعد إضافة إعدادات الميديا

60- go to [templates/pages/about.html] and append:

<form method="POST">
        {% csrf_token %}
        <input type="text" name="username" placeholder="Username"/>
        <input type="password" name="password" placeholder="Password"/>
        <input type="submit" value="submit"/>
</form>


61- go to [models.py] into [pages] and write:

from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

62- go to [views.py] into [pages] and write:

from django.shortcuts import render
from .models import Login

def index(request):
    return render(request, 'pages/index.html', {'name':''})

def about(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    data = Login(username=username, password=password)
    data.save()

    return render(request, 'pages/about.html', {'name':''})


63- create file [forms.py] into [pages] app and write:

from django import forms

class LoginForm(forms.Form):
    usernames = forms.CharField(max_length=50)
    passwords = forms.CharField(max_length=50)

ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
64- final form:
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
1- in [admin.py] into [pages] app:

from django.contrib import admin
from .models import Login

admin.site.register(Login)

ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
2- in [models.py] into [pages] app:

from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=100,default="ali")
    password = models.CharField(max_length=100,default="123")

ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
3- in [forms.py] into [pages] app:

from django import forms
from .models import Login
class LoginForm(forms.ModelForm): 
    class Meta:
        model = Login
        fields = '__all__'
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
4- in [views.py] into [pages] app: 

from django.shortcuts import render
from .models import Login
from .forms import LoginForm

def index(request):
    return render(request, 'pages/index.html', {'name':''})

def about(request):
    if request.method == 'POST':
        dataform = LoginForm(request.POST)
        if dataform.is_valid():
            dataform.save()

    return render(request, 'pages/about.html', {'lf':LoginForm})
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ


عندما تريد ربط ماي اس كيو إل مع دجانغو 
65- install xampp

66- and write in [settings.py]:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
        
    }
}



67- python manage.py migrate


68- when I want to rename the project [firstproject](name_project):
1- go to [firstproject/manage.py]:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ


2- go to [firstproject/firstproject/asgi.py]:

#comment line 2:
#ASGI config for firstproject project. 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings') #line 14
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ


3- go to [firstproject/firstproject/settings.py]:
#comment line 2:
#Django settings for firstproject project.
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
#line 54:
ROOT_URLCONF = 'firstproject.urls'
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
#line 72:
WSGI_APPLICATION = 'firstproject.wsgi.application'
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
#line 133:
os.path.join(BASE_DIR, 'firstproject/static'),
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ


4- go to [firstproject/firstproject/urls.py]
#comment
#line 1:
firstproject URL Configuration

ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ



5- go to [firstproject/firstproject/wsgi.py]
#comment line 2:
#WSGI config for firstproject project.
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
line 14:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ




69- الملفات التي ننشئها داخل المجلد الأصلي للمشروع هي:

templates - 19-22
media - 57-59
static - ننسخه من مجلد المشروع الابن بأوامر كتبتها في الأعلى في هذا الملف رقم من 30-34
photos




