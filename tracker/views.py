from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import AssignmentForm # type: ignore
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


def all_assignments(request):
    assigned = [
        {
            "id": 1,
            "title": "Math Assignment 1",
            "subject": "Mathematics",
            "deadline": "2025-05-10 23:59",
            "priority": "High"
        },
        {
            "id": 2,
            "title": "Science Project",
            "subject": "Science",
            "deadline": "2025-05-12 18:00",
            "priority": "Medium"
        }
    ]
    
    submitted = [
        {
            "id": 3,
            "title": "History Essay",
            "subject": "History",
            "deadline": "2025-05-05 23:59",
            "grade": "A-"
        }
    ]
    
    return render(request, 'all_assignments.html', {
        'assigned': assigned,
        'submitted': submitted,
        'missed': [],
        'hidden': []
    })

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
            assignment = form.save(commit=False)
            assignment.faculty = request.user.faculty  # Adjust if different
            assignment.save()
            messages.success(request, 'Assignment uploaded successfully!')
            return redirect('add_assignment')
    else:
        form = AssignmentForm()
    return render(request, 'tracker/add_assignment.html', {'form': form})
