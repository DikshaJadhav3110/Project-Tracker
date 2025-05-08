from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from .forms import AssignmentForm, AssignmentSubmissionForm # type: ignore
from .models import Assignment, AssignmentSubmission
from django.contrib import messages
from django.contrib.auth import logout
from django.utils import timezone  # Add this import


@login_required
def dashboard(request):
    user = request.user

    if user.groups.filter(name='Student').exists():
        submissions = AssignmentSubmission.objects.filter(student=request.user).select_related('assignment')
        context = {
        'submissions': submissions,
        'student_name': request.user.get_full_name() or request.user.username
        }
        return render(request, 'student.html', context)

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
    # assignments = [
    #     {
    #         "title": "Math Assignment 1",
    #         "subject": "Mathematics",
    #         "description": "Solve all questions from chapter 2.",
    #         "priority": "High",
    #         "deadline": "2025-05-10 23:59",
    #         "pdf_url": "https://example.com/sample.pdf",
    #     },
    #     {
    #         "title": "Science Project",
    #         "subject": "Science",
    #         "description": "Prepare a model of the solar system.",
    #         "priority": "Medium",
    #         "deadline": "2025-05-12 18:00",
    #         "pdf_url": "https://example.com/sample2.pdf",
    #     },
    # ]
    # return render(request, 'studentview.html', {"assignments": assignments})
    pass



@login_required
def student_assignment_detail(request, submission_id):
    submission = get_object_or_404(AssignmentSubmission, id=submission_id, student=request.user)
    
    if request.method == 'POST':
        form = AssignmentSubmissionForm(request.POST, request.FILES, instance=submission)
        if form.is_valid():
            # Update submission fields
            submission = form.save(commit=False)
            submission.status = 'submitted'
            submission.grade_status = 'pending'
            submission.submission_time = timezone.now()
            submission.save()
            
            # messages.success(request, 'Assignment submitted successfully!')
            return redirect('student_dashboard')  # Make sure this URL name matches your URLs
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AssignmentSubmissionForm(instance=submission)
    
    context = {
        'assignment': submission.assignment,
        'submission': submission,
        'form': form,
        'student_name': request.user.get_full_name() or request.user.username
    }
    return render(request, 'student_assignment_detail.html', context)




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


@login_required
def student_dashboard(request):
    # Get all submissions for the current student
    submissions = AssignmentSubmission.objects.filter(student=request.user).select_related('assignment')
    
    context = {
        'submissions': submissions,
        'student_name': request.user.get_full_name() or request.user.username
    }
    return render(request, 'student.html', context)







@login_required
def scheduled_assignments(request):
    # Get assignments for the logged-in faculty
    assignments = Assignment.objects.filter(faculty=request.user)
    context = {
        'assignments': assignments,
        'faculty_name': request.user.first_name
    }
    return render(request, 'scheduled_assignments.html', context)

@login_required
def faculty_assignment_detail(request, assignment_id):
    # Get specific assignment
    assignment = get_object_or_404(Assignment, id=assignment_id, faculty=request.user)
    
    # Get submissions for this assignment
    submissions = AssignmentSubmission.objects.filter(assignment=assignment)
    
    context = {
        'assignment': assignment,
        'submissions': submissions,
        'faculty_name': request.user.first_name
    }
    return render(request, 'assignment_detail.html', context)

@login_required
def submission_detail(request, submission_id):
    # Get specific submission
    submission = get_object_or_404(AssignmentSubmission, id=submission_id)
    
    context = {
        'submission': submission,
        'faculty_name': request.user.first_name
    }
    return render(request, 'submission_detail.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')  # Assuming you have a login URL named 'login'