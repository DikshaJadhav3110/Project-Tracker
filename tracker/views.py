from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .forms import AssignmentForm # type: ignore
from .models import Assignment, AssignmentSubmission
from django.contrib import messages


@login_required
def dashboard(request):
    user = request.user

    if user.groups.filter(name='Student').exists():
        return render(request, 'student.html')

    elif user.groups.filter(name='Faculty').exists():
        return render(request, 'faculty.html')

    else:
        return render(request, 'unknown_role.html')  # fallback


def all_assignments(request):
    assignments = Assignment.objects.all().order_by('-created_at')
    context = {
        'assignments': assignments
    }
    return render(request, 'tracker/all_assignments.html', context)



def studentview(request):
    assignments = [
        {
            "title": "Math Assignment 1",
            "subject": "Mathematics",
            "description": "Solve all questions from chapter 2.",
            "priority": "High",
            "deadline": "2025-05-10 23:59",
            "pdf_url": "https://example.com/sample.pdf",
        },
        {
            "title": "Science Project",
            "subject": "Science",
            "description": "Prepare a model of the solar system.",
            "priority": "Medium",
            "deadline": "2025-05-12 18:00",
            "pdf_url": "https://example.com/sample2.pdf",
        },
    ]
    return render(request, 'studentview.html', {"assignments": assignments})


def assignment_detail(request, assignment_id):
    assignments = {
        1: {
            "title": "Math Assignment 1",
            "subject": "Mathematics",
            "description": "Solve all questions from chapter 2.",
            "priority": "High",
            "deadline": "2025-05-10 23:59",
            "pdf_url": "https://example.com/sample.pdf",
        },
        # Add more assignments
    }
    assignment = assignments.get(assignment_id)
    return render(request, 'tracker/assignment_detail.html', {"assignment": assignment})




def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the assignment first
            assignment = form.save(commit=False)
            assignment.faculty = request.user # Assuming faculty is logged in
            assignment.faculty_name = request.user.first_name
            assignment.save()
            
            # Get all users in the "Student" group
            students = Group.objects.get(name="Student").user_set.all()
            
            # Create AssignmentSubmission for each student
            for student in students:
                AssignmentSubmission.objects.create(
                    assignment=assignment,
                    student=student,
                    faculty=request.user,
                    faculty_name=request.user.first_name,
                    status='not submitted',
                    grade_status='not submitted',
                    grade=0,
                    priority='Medium',
                    hidden=False,
                    missed=False,
                    student_name=student.first_name
                )
            
            # messages.success(request, 'Assignment created successfully! Submission records created for all students.')
            return redirect('faculty_home')   # Redirect to assignments list page
    else:
        form = AssignmentForm()
    
    return render(request, 'add_assignment.html', {'form': form})


def faculty_home(request):
    return render(request, 'faculty.html')