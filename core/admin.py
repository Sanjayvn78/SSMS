from django.contrib import admin
from .models import Timetable, Assignment, Note, Expense, Result, CustomUser

admin.site.register(CustomUser)
admin.site.register(Timetable)
admin.site.register(Assignment)
admin.site.register(Note)
admin.site.register(Expense)
admin.site.register(Result)


from django.contrib import admin
from .models import Student, Attendance

admin.site.register(Student)
admin.site.register(Attendance)