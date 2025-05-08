from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('studentview/', views.studentview, name='studentview'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'), 
    path('all-assignments/', views.all_assignments, name='all_assignments'),
    path('assignment/<int:submission_id>/', views.student_assignment_detail, name='student_assignment_detail'),
    path('add-assignment/', views.add_assignment, name='add_assignment'),
    path('faculty/', views.faculty_home, name='faculty_home'),
    path('scheduled_assignments/', views.scheduled_assignments, name='scheduled_assignments'),
    path('faculty/assignment/<int:assignment_id>/', views.faculty_assignment_detail, name='faculty_assignment_detail'),
    path('student/assignment/<int:submission_id>/', views.student_assignment_detail, name='student_assignment_detail'),
    path('submission/<int:submission_id>/', views.submission_detail, name='submission_detail'),
    path('logout/', views.logout_view, name='logout'),
]

