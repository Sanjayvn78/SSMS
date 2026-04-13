from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from .models import *

@csrf_protect
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        confirm = request.POST.get('confirm_password')

        if confirm:
            if password == confirm:
                User.objects.create_user(username=username, password=password)
                return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if role == 'student':
                return redirect('student_home')
            return redirect('teacher_home')

    return render(request, 'login.html')


def student_home(request):
    return render(request, 'student_home.html')


def teacher_home(request):
    return render(request, 'teacher_home.html')


# ASSIGNMENT
def upload_assignment(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')

        Assignment.objects.create(
            title=title,
            description=description,
            deadline=deadline
        )

        return redirect('upload_assignment')

    data = Assignment.objects.all()
    return render(request, 'upload_assignment.html', {'data': data})


def assignments(request):
    from datetime import date
    data = Assignment.objects.all()
    return render(request, 'assignments.html', {'assignments': data, 'today': date.today()})


def delete_assignment(request, id):
    if request.method == "POST":
        Assignment.objects.filter(id=id).delete()
    return redirect('upload_assignment')


# NOTES
def upload_notes(request):
    if request.method == "POST":
        Note.objects.create(
            subject=request.POST.get('subject'),
            content=request.POST.get('content'),
            video_link=request.POST.get('video_link'),
            file=request.FILES.get('file')
        )
        return redirect('upload_notes')

    data = Note.objects.all()
    return render(request, 'upload_notes.html', {'data': data})


def notes(request):
    data = Note.objects.all()
    return render(request, 'notes.html', {'notes': data})

def delete_note(request, id):
    if request.method == "POST":
        Note.objects.filter(id=id).delete()
        return redirect('upload_notes')
    return redirect('upload_notes')


# TIMETABLE
def upload_timetable(request):
    if request.method == "POST":
        Timetable.objects.create(
            day=request.POST.get('day'),
            p1=request.POST.get('p1'),
            p2=request.POST.get('p2'),
            p3=request.POST.get('p3'),
            p4=request.POST.get('p4'),
            p5=request.POST.get('p5'),
            p6=request.POST.get('p6'),
            p7=request.POST.get('p7'),
        )
        return redirect('upload_timetable')

    data = Timetable.objects.all()
    return render(request, 'upload_timetable.html', {'data': data})


def timetable(request):
    data = Timetable.objects.all()
    return render(request, 'timetable.html', {'timetable': data})


def delete_timetable(request, id):
    if request.method == "POST":
        Timetable.objects.filter(id=id).delete()
        return redirect('upload_timetable')
    return redirect('upload_timetable')


# RESULTS
def manage_results(request):
    if request.method == "POST":
        Result.objects.create(
            subject=request.POST.get('subject'),
            marks=request.POST.get('marks')
        )
        return redirect('manage_results')

    data = Result.objects.all()
    return render(request, 'manage_results.html', {'data': data})


def results(request):
    results_data = Result.objects.all()
    return render(request, 'results.html', {'results': results_data})


def delete_result(request, id):
    if request.method == "POST":
        Result.objects.filter(id=id).delete()
        return redirect('manage_results')
    return redirect('manage_results')

def expenses(request):
    if request.method == 'POST':
        item = request.POST.get('title')
        amount = request.POST.get('amount')

        Expense.objects.create(item=item, amount=amount)

        return redirect('expenses')   # ✅ NOT assignments

    data = Expense.objects.all()
    total = sum(e.amount for e in data)

    return render(request, 'expenses.html', {
        'expenses': data,
        'total': total
    })
def student_assignments(request):
    assignments = Assignment.objects.all()

    if request.method == "POST":
        assignment_id = request.POST.get("assignment_id")
        file = request.FILES.get("file")

        Submission.objects.create(
            assignment_id=assignment_id,
            student_name=request.user.username,
            file=file
        )

        return redirect('student_assignments')

    return render(request, 'student_assignments.html', {
        'assignments': assignments
    })
def view_submissions(request):
    submissions = Submission.objects.all()
    return render(request, 'view_submissions.html', {
        'submissions': submissions
    })
from django.shortcuts import render, redirect
from .models import Assignment, Submission


# 👨‍🎓 STUDENT VIEW ASSIGNMENTS
def assignments(request):
    data = Assignment.objects.all()
    return render(request, 'assignments.html', {'assignments': data})


# 📥 STUDENT SUBMIT
def submit_assignment(request, id):
    assignment = Assignment.objects.get(id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        file = request.FILES.get('file')

        Submission.objects.create(
            assignment=assignment,
            student_name=name,
            file=file
        )
        return redirect('assignments')

    return render(request, 'student_assignments.html', {'a': assignment})


# 👨‍🏫 TEACHER VIEW SUBMISSIONS
def view_submissions(request):
    data = Submission.objects.all()
    return render(request, 'view_submissions.html', {'data': data})
from django.shortcuts import render
from .models import Student, Attendance

def attendance_report(request):
    students = Student.objects.all()

    data = []

    for s in students:
        total = Attendance.objects.filter(student=s).count()
        present = Attendance.objects.filter(student=s, status="Present").count()

        percentage = (present / total * 100) if total > 0 else 0

        data.append({
            "name": s.student_name,
            "total": total,
            "present": present,
            "percentage": round(percentage, 2)
        })

    return render(request, "attendance.html", {"data": data})
from django.shortcuts import render
from .models import Student, Attendance

def attendance_report(request):
    students = Student.objects.all()
    data = []

    for s in students:
        total = Attendance.objects.filter(student=s).count()
        present = Attendance.objects.filter(student=s, status="Present").count()

        percentage = (present / total * 100) if total > 0 else 0

        data.append({
            "name": s.student_name,
            "total": total,
            "present": present,
            "percentage": round(percentage, 2)
        })

    return render(request, "attendance.html", {"data": data})