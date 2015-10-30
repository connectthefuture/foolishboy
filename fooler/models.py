#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class question(models.Model):
#	quser=models.ForeignKey(UserProfile)
	qtitle=models.CharField(max_length=1024,unique=False)
	qtime=models.DateTimeField(auto_now=True)
	qbonus=models.IntegerField(default=5)

	def __unicode__(self):
		return self.qtitle

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	bonus = models.IntegerField(default=0)

	def __unicode__(self):
		return self.user.username

class answers(models.Model):
	qtitle=models.ForeignKey(question)
	qanswer=models.CharField(max_length=1024)


	def __unicode__(self):
		return self.qanswer
