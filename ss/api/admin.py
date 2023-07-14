from django.contrib import admin
from .models import Students
from .models import Teachers, UserRoles, PresentStudent, TimeTable, Subjects, SubjectTeacher

# Register your models here.

admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(UserRoles)
admin.site.register(PresentStudent)
admin.site.register(TimeTable)
admin.site.register(Subjects)
admin.site.register(SubjectTeacher)
