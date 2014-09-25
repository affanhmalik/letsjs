from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from django.http import HttpResponse

# Create your views here.


# The main authentication function for a registered user, the success and fail redirects can be changed
def auth_and_login(request, onsuccess='/main/home/', onfail='/main/signup/'):
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	if user is not None:
		login(request, user)
		return redirect(onsuccess)
	else:
		return redirect(onfail)

def sign_up_in(request):
	post = request.POST
	if not user_exists(post['username']):
		user = create_user(username=post['username'], password=post['password'])
		
		return auth_and_login(request)
	else:
		return redirect("/main/")

@login_required
def loggedin(request):
	return render_to_response('main/test.html',{'user':request.user})


# Create a new user with the request credentials
def create_user(username,password):
	user = User(username=username)
	user.set_password(password)
	user.save()
	return user

# Check to see if username exists or not
def user_exists(username):
	user_count = User.objects.filter(username=username).count()
	if user_count == 0:
		return False
	return True

def logout_user(request):
	logout(request)
	return redirect("/main/")