from django.shortcuts import render
from django.contrib.auth.models import User
from facultyapp.models import Marks
from adminapp.models import StudentList


def homepage(request):
    return render(request, 'HomePage.html')


def student_home_page(request):
    return render(request, 'studentapp/StudentHomePage.html')


def view_marks(request):
    user = request.user
    try:
        # Ensure the username corresponds to Register_Number
        student = StudentList.objects.get(Register_Number=user.username)

        # Retrieve marks for the student
        marks = Marks.objects.filter(student=student)

        return render(request, 'studentapp/view_marks.html', {'marks': marks})
    except StudentList.DoesNotExist:
        return render(request, 'studentapp/no_studentlist.html', {
            'error': 'No student record found for this user.'
        })
    except Exception as e:
        return render(request, 'studentapp/no_studentlist.html', {
            'error': str(e)
        })
