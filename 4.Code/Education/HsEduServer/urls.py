#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HsEduServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from HsEdu.Api.WebCenterApi import *
from HsEdu.Api.ThirePart.WxApiHelp import *
from HsEdu.Api.Custom.CustomApi import *
from HsEdu.Api.Chat.ChatApi import *
from HsEdu.Api.Admin.AdminApi import *

urlpatterns = [
    # API接口
    url(r'^admin/', admin.site.urls),
    url(r'^$',WebCenterApi.goHome),

    # 启动时微信登录---等待页面
    url(r'^wait.html',WebCenterApi.openWaitPage),

    # 首页大菜单
    url(r'^my_message.html',WebCenterApi.openPage1),
    url(r'^resource_store.html',WebCenterApi.openPage2),
    url(r'^service_store.html',WebCenterApi.openPage3),
    url(r'^user_center.html',WebCenterApi.openPage4),

    # 微信授权
    url(r'^MP_verify_iJqJ8ZXNRFKMeimo.txt', WxApiHelp.getWxAuthData),
    url(r'^wxauth.html', WxApiHelp.wxA),

    # 客户api
    url(r'^api/ctm/$',CustomApi.CommandDispatch),

    # 消息页面
    url(r'^msg_chat.html',ChatApi.CommandDispatch),
    url(r'^msg_subList.html',ChatApi.CommandDispatch),
    url(r'^msg_view.html',ChatApi.CommandDispatch),
    url(r'^res_detail.html',CustomApi.CommandDispatch),
    url(r'^srv_detail.html',CustomApi.CommandDispatch),
    url(r'^view_remark.html',CustomApi.CommandDispatch),

    # 用户dns
    url(r'^res_order.html',CustomApi.CommandDispatch),
    url(r'^order_detail_info.html', CustomApi.CommandDispatch),
    url(r'^cooperation.html', CustomApi.CommandDispatch),
    url(r'^suggest.html', CustomApi.CommandDispatch),
    url(r'^mycheck.html', CustomApi.CommandDispatch),



    # 管理页面
    url(r'^admin.html',AdminApi.CommandDispatch),
    url(r'^gettestData/$',AdminApi.getTestData),


] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)