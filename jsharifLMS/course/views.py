from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from course.models import Course, Department, User_log
from django.contrib.auth.decorators import login_required

#create your view here


def view_course_list(request):
	if request.user.is_authenticated:
		course_list = Course.objects.all()
		return render(request, "course_list.html", {'UName': request.user.username, 'course_list_ds':course_list})
	else:
		return HttpResponseRedirect("/login/") 


def view_course_detail(request, offset):
	#offset == Departmentid
	course_detail = Course.objects.get(id = int(offset))
	return render(request, "course_detail.html", {'course_detail_ds':course_detail})

@login_required(login_url = "/login")
def view_department_list(request):
	obj = User_log()
	obj.user
	obj.action
	obj.save()
	
	department_list = Department.objects.all()
	return render(request, "department_list.html", {'department_list_ds':department_list})




	'''
	return HttpResponse("<h2>Here, You can see list of course</h2>"+
	"<ul>"
		"<li>Course Code: 101, Course Name: Pyhton</li>" + 
		"<li>Course Code: 102, Course Name: Django</li>" +
		"<li>Course Code: 103, Course Name: Data Science</li>" +
	"</ul>")
	'''