from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Student model (linked to auth User)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user.username

# Faculty model (linked to auth User)
class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user.username

# Assignment created by faculty
class Assignment(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='assignments')
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    possible_grades = models.CharField(max_length=100)
    upload_pdf = models.FileField(upload_to='assignments/')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.subject}"

# Assignment Submission by students
class AssignmentSubmission(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('not submitted', 'Not Submitted'),
    ]

    GRADE_STATUS_CHOICES = [
        ('0', '0'),
        ('assigned', 'Assigned'),
        ('pending', 'Pending'),
        ('not submitted', 'Not Submitted'),
    ]

    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='graded_submissions')

    submitted_pdf = models.FileField(upload_to='submissions/', null=True, blank=True)
    submission_time = models.DateTimeField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not submitted')
    grade_status = models.CharField(max_length=20, choices=GRADE_STATUS_CHOICES, default='not submitted')
    grade = models.IntegerField(default=0)

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    hidden = models.BooleanField(default=False)
    missed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.assignment.title} - {self.student.user.username}"
