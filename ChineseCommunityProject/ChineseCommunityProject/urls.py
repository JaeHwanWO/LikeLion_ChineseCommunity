"""ChineseCommunityProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import ChineseApp.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', ChineseApp.views.func, name='main'),
    path('home/', ChineseApp.views.home, name='home'),
    path('create/', ChineseApp.views.create, name='create'),
    path('new/', ChineseApp.views.new, name='new'),
    path('posting/<int:posting_id>/', ChineseApp.views.detail, name='detail'),
    path('login/', accounts.views.login, name='login'),
    path('signup/', accounts.views.signup, name='signup'),
    path('logout/', accounts.views.logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# API 2개
# 1. POST /users/signup : 회원가입 후 인증메일 전송
# 2. GET /users/activate : 인증 메일 클릭 시 해당 아이디를 활성화
urls.py에 path 추가해준다.
path('signup', views.SignUp.as_view(), name='signup')
path('activate/<str:uidb64>/<str:token>', views.UserActivate.as_view(), name='activate')

1. 회원가입 후 이메일 전송
views.py에 class 만든다.
