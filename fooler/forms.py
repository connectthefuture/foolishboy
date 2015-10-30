#coding:utf-8
from django import forms
from fooler.models import question,UserProfile,answers
from django.contrib.auth.models import User
import datetime
import django.utils.timezone as timezone
class questionForm(forms.ModelForm):
	qtitle=forms.CharField(max_length=1024,widget=forms.Textarea(attrs={'class':"form-control",'rows':3}))
	qbonus=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	qtime=forms.DateTimeField(widget=forms.HiddenInput(),required=False)
	class Meta:
		model=question
		fields=('qtitle',)	




class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class  Meta:
		model = User
		fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('bonus',)
			
		
			
		
