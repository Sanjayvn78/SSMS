from django.urls import path
from . import views

urlpatterns = [
    # Login
    path('', views.login_page, name='login'),

    

    # Student pages
    path('student_home/', views.student_home, name='student_home'),
    path('timetable/', views.timetable, name='timetable'),
    path('assignments/', views.assignments, name='assignments'),
    path('notes/', views.notes, name='notes'),
    path('expenses/', views.expenses, name='expenses'),
    path('results/', views.results, name='results'),
    path('student_assignments/', views.student_assignments, name='student_assignments'),
    path('submit/<int:id>/', views.submit_assignment, name='submit_assignment'),
    path('submissions/', views.view_submissions, name='submissions'),
   

    # Teacher pages
    path('teacher_home/', views.teacher_home, name='teacher_home'),
    path('upload_assignment/', views.upload_assignment, name='upload_assignment'),
    path('upload_notes/', views.upload_notes, name='upload_notes'),
    path('upload_timetable/', views.upload_timetable, name='upload_timetable'),
    path('manage_results/', views.manage_results, name='manage_results'),

    # Delete actions
    path('delete_assignment/<int:id>/', views.delete_assignment, name='delete_assignment'),
    path('delete_note/<int:id>/', views.delete_note, name='delete_note'),
    path('delete_timetable/<int:id>/', views.delete_timetable, name='delete_timetable'),
    path('delete_result/<int:id>/', views.delete_result, name='delete_result'),
    path('results/', views.student_result, name='results'),

]
