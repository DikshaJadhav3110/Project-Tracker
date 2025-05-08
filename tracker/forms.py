from django import forms
from .models import Assignment, AssignmentSubmission

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['subject', 'title', 'description', 'possible_grades', 'upload_pdf', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'subject': forms.TextInput(attrs={'placeholder': 'Enter subject name'}),
        }

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ['submitted_pdf', 'submitted_video', 'submitted_zip']
        widgets = {
            'submitted_pdf': forms.FileInput(attrs={'accept': '.pdf'}),
            'submitted_video': forms.FileInput(attrs={'accept': 'video/*'}),
            'submitted_zip': forms.FileInput(attrs={'accept': '.zip,.rar,.7z'}),
        }

