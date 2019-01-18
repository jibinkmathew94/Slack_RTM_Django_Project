"""slack_jukebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView
from video_upvote.views import HomeView, upvote
from user.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    path('upvote', upvote),
    path('signup', signup),
    # re_path(r'^upvote/(?P<id>[0-9].)$')
]
