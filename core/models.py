from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class Timetable(models.Model):
    day = models.CharField(max_length=20)
    p1 = models.CharField(max_length=50, blank=True)
    p2 = models.CharField(max_length=50, blank=True)
    p3 = models.CharField(max_length=50, blank=True)
    p4 = models.CharField(max_length=50, blank=True)
    p5 = models.CharField(max_length=50, blank=True)
    p6 = models.CharField(max_length=50, blank=True)
    p7 = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.day


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()


class Note(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='notes/', null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)


class Expense(models.Model):
    item = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class Result(models.Model):
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.student_name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.CharField(max_length=10)  # Present / Absent

def __str__(self):
        return f"{self.student.student_name} - {self.status}"
        from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)