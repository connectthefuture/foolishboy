#coding:utf-8
from django.shortcuts import render
from fooler.models import question,answers
from fooler.forms import questionForm,UserForm,UserProfileForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#from django.http import HttpResponse
# Create your views here.

def index(request):
#	values=request.META.items()
#	values.sort()
#	html=[]
#	for k,v in values:
#		html.append("<tr><td>%s</td><td>%s</td></tr>"%(k,v))
#	return HttpResponse("<table>%s</table>"%'\n'.join(html))
	question_list=question.objects.order_by('-qtime')[:20]
	context_dict={'questions':question_list}
	return render(request,'fooler/index.html',context_dict)

@login_required
def answer(request):
#	question_list=question.objects.order_by('-qtime')[:20]
#	context_dict={'questions':question_list}
	return render(request,'fooler/b.html')

@login_required
def add_question(request):
	if request.method == 'POST':
		form=questionForm(request.POST)
		if form.is_valid():
			form.save(commit=True)

			return index(request)
		else:
			print form.errors
	else:
		form=questionForm()
	return render(request,'fooler/b.html',{'form':form})

def register(request):
	registered=False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			registered = True

		else:
			print user_form.errors,profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request,'fooler/register.html',
					{'user_form':user_form,
					'profile_form':profile_form,
					'registered':registered})


def user_login(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/fooler')
			else:
				return HttpResponse("your fooler accout is disabled.")
		else:
			print "Invalid login details:{0},{1}".format(username,password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request,'fooler/login.html',{})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/fooler/')

def quest(request,qid):
	ques=question.objects.get(id=qid)
	answer_list=ques.answers_set.all()
	context_dict={"quest":ques,"answers":answer_list}
	return render(request,'fooler/question.html',context_dict)

def huifu (request):
	strs=request.POST.get('a')
	ids=request.POST.get('b')
	ques=question.objects.get(id=ids)
	qanswer=answers(qtitle=ques,qanswer=strs)
	qanswer.save()
	answer_list=ques.answers_set.all()
	context_dict={"quest":ques,"answers":answer_list}
	return render(request,'fooler/question.html',context_dict)
	
