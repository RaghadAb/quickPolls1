from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Poll,Options

def index(request):
	return render(request,'index.html')
	
def header(request):
	return render(request,'header.html')
	
def login(request):
	return render(request,'login.html')
	
def register(request):
	return render(request,'register.html')

def createpoll(request):
	return render(request,'createpoll.html')

def myaccount(request):
	return render(request,'myaccount.html')

def mypolls(request):
	return render(request,'mypolls.html')

def search(request):
	polls= Poll.objects.all()
	context={'polls':polls}
	return render(request,'search.html',context)

def vote(request, quiPoll_id):
	poll = get_object_or_404(Poll, id=quiPoll_id)
	return render(request,'vote.html')

def results(request):
	return render(request,'results.html')
	
def all_urls(request):
	return render(request,'all_urls.html')
	
def option_Number(request, quiPoll_id):
    option=Poll.objects.get(id=quiPoll_id)

    if request.method=="POST":
        print("It's submitted!")
        print(request.POST)

    if request.method=="GET":
        print("Got it")
        print(request.GET)

    context={'option':option}
    return render(request,'option_Number.html',context)