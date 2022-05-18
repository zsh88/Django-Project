"""jsharifLMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin

#from course.views import index, home, aboutUS, welcome2
from user.views import login, logout, show_register_form, save_user, update_profile, show_profile, show_home
from course.views import view_course_list, view_department_list,view_course_detail
#from django.urls import path
#from company.views import about_us, contact_us


urlpatterns = [
    url('admin/', admin.site.urls),
    #url('^$', index),
    #url('^home/$', home),
    url('^login/$', login),
    url('^logout/$', logout),
    url('^profile/$', show_profile),
    url('^home/$', show_home),
    url('^register/$', show_register_form),
    url('^save_user/$', save_user),
    url('^update_profile/$', update_profile),
    url('^show_course_list/$', view_course_list),
    url('^show_department_list/$', view_department_list),
    url('^show_course/(\d+)$', view_course_detail),
    #url('^about_us/$', about_us),
    #url('^contact_us/$', contact_us),
]
    

