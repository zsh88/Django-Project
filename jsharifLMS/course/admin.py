from django.contrib import admin
from course.models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=('code', 'title','department_id')
    search_fields = ('title',)
    list_filter = ('code',)
    
admin.site.register(Course, CourseAdmin)


