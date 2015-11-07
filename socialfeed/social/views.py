from django.shortcuts import render
from django.http import HttpResponse
from .models import Auth
# Create your views here.

def index(request):
	latest_list = Auth.objects.all()
	context = {'ll' : latest_list}
	return render(request, 'social/login.html', context)
def signup(request):
	return render(request, 'social/signup.html', {})
