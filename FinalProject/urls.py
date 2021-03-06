"""FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from rockClimbers import views as rockView

urlpatterns = [
    path('', rockView.home, name='home'),
    path('create-post/', rockView.create_post, name="create_post"),
    path('create-comment/<int:post_id>/', rockView.create_comment,
         name="create_comment"),
    path('post-detail/<int:post_id>/', rockView.post_detail,
         name="post-detail"),
    path('admin/', admin.site.urls),
]
