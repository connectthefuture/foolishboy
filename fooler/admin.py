#coding:utf-8
from django.contrib import admin
from fooler.models import question
from fooler.models import UserProfile
# Register your models here.
admin.site.register(question)
admin.site.register(UserProfile)

