from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#define function
'''
def name (request):
	return HttpResponse('<h1> Index Page ... in Course App </h1>')

'''

# Create your views here.

def login(request):
	return render(request, "login.html")
	
	
	#return render_to_response("login.html")
	#return HttpResponse(
	#	"<a href='/register'>register</a> <br> <a href='/show_profile'>show_profile</a> <br> <a href='/logout'>logout</a>"
	#	+"<h1> Login User </h1>")

def show_home(request):
	username = request.POST.get("username", "")
	password = request.POST.get("password", "")
	#username = request.POST["username"]
	#password = request.POST["password"]
	userObject = auth.authenticate(username=username, password=password)
	if userObject:
		auth.login(request, userObject)
		return HttpResponseRedirect("/show_department_list/")
		#return HttpResponse("<h1> Check Username & Password .... <br> Login Succeed  </h1>") 
	else:
		return HttpResponse("<h1> Login Failed </h1>") 


def logout(request):
	auth.logout(request)
	return render(request, "logout.html")
	#return render_to_response("logout.html")
	#return HttpResponse(
	#	"<a href='/register'>register</a> <br> <a href='/show_profile'>show_profile</a> <br> <a href='/logout'>logout</a>"
	#	+ '<h1> Logout User </h1>')

def show_register_form(request):
	return render(request, "register.html")
	#return HttpResponse(
	#	"<a href='/register'>register</a> <br> <a href='/show_profile'>show_profile</a> <br> <a href='/logout'>logout</a>"
	#	+'<h1> Register User </h1>')

def save_user(request):
	username = request.POST.get("username", "")
	password = request.POST.get("password", "")
	email = request.POST.get("email", "")
	user_object = User.objects.create_user(username, email, password)

	user_object.is_activate = False
	user_object.save()
	
	return HttpResponse("<h1>User Save, Login Again ...</h1>")

@login_required(login_url = "/login")
def show_profile(request):
	Username = request.user.username
	FirstName = request.user.first_name
	LastName = request.user.last_name
	Email = request.user.email

	return render(request, "profile.html", {'Username':Username, 'FirstName':FirstName, "LastName":LastName, "Email":Email})
	#return HttpResponse(
	#	"<a href='/register'>register</a> <br> <a href='/show_profile'>show_profile</a> <br> <a href='/logout'>logout</a>"
	#	+'<h1> Show Profile</h1>')
@login_required(login_url = "/login")
def update_profile(request):
	FName = request.POST.get("firstname", "")
	LName = request.POST.get("lastname", "")
	Email = request.POST.get("email", "")
	UName = request.User.username

	Object_User = User.objects.get(username = UName)
	Object_User.first_name = FName
	Object_User.last_name = LName
	Object_User.email = Email
	Object_User.save()

	return HttpResponse("<h1>user profile is updated</h1>")





