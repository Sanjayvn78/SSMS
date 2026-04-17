from django.contrib import admin
from .models import CustomUser, Timetable, Assignment, Submission, Note, Expense, Result, Student

admin.site.register(CustomUser)
admin.site.register(Timetable)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Note)
admin.site.register(Expense)
admin.site.register(Result)
admin.site.register(Student)