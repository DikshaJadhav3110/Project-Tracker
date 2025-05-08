from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('studentview/', views.studentview, name='studentview'),
    path('all-assignments/', views.all_assignments, name='all_assignments'),
    path('assignment_detail/', views.assignment_detail, name='assignment_detail'),
    path('add-assignment/', views.add_assignment, name='add_assignment'),
    path('faculty/', views.faculty_home, name='faculty_home'),
]

