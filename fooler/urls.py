#coding:utf-8
from django.conf.urls import patterns,url
from fooler import views

urlpatterns=patterns('',
	url(r'^$',views.index,name='index'),
	url(r'^huida',views.answer,name='answer'),
	url(r'^add_question',views.add_question,name='add'),
	url(r'^register',views.register,name='register'),
	url(r'^login',views.user_login,name='login'),
	url(r'^logout',views.user_logout,name='logout'),
	url(r'^([\d]+)',views.quest,name='logout'),
	url(r'^huifu',views.huifu,name='logout'),
#	url(r'^ajax',views.ajax,name='ajax'),
)	
