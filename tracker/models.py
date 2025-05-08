from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Assignment created by faculty
class Assignment(models.Model):
    faculty = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments')
    faculty_name = models.CharField(max_length=150, default='0')
    title = models.CharField(max_length=200)
    description = models.TextField()
    subject = models.CharField(max_length=100, default='')
    possible_grades = models.IntegerField()
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
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=150, default='0')
    faculty = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    faculty_name = models.CharField(max_length=150, default='0')


    submitted_pdf = models.FileField(upload_to='submissions/', null=True, blank=True)
    submitted_video = models.FileField(upload_to='submissions/videos/', null=True, blank=True)
    submitted_zip = models.FileField(upload_to='submissions/zips/', null=True, blank=True)
    submission_time = models.DateTimeField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not submitted')
    grade_status = models.CharField(max_length=20, choices=GRADE_STATUS_CHOICES, default='not submitted')
    grade = models.IntegerField(default=0)

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    hidden = models.BooleanField(default=False)
    missed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.assignment.title} - {self.student.username}"  # Remove .user
