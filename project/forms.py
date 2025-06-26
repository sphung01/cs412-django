# File: project/forms.py
# Author: Steven Phung (sphung01@bu.edu), 6/25/2025
# Description: In this file, we create forms where they
# handle user input and pass it over to the database
# through Django's ModelForm.

from django import forms
from .models import *

class CreateUserForm(forms.ModelForm):
    """
        Helps create a form that will display all of the fields of the
        ProjectUser model.
    """

    class Meta:
        """
            Associate this form with a ProjectUser model from our database.
        """
        model = ProjectUser
        fields = ['first_name', 'last_name', 'email', 'role', 'student_id', 'profile_image']

class CreateEnrollmentForm(forms.ModelForm):
    """
        Displays a form that will allow user to enter a code to join class.
    """

    join_class_code = forms.CharField(label="Enter Code", max_length=6, required=True)

    class Meta:
        """
            Associates this form with the Enrollment model from the database
        """

        model = Enrollment
        fields = ['join_class_code']

class CreateReportForm(forms.ModelForm):
    """
        Allows the student to enter code to let teacher know that
        they are present in class.
    """

    attendance_code = forms.CharField(label="Enter Code", max_length=6, required=True)

    class Meta:
        """
            Associates this form with the Report model from the database
        """

        model = Report
        fields = ['attendance_code']

class CreateCourseForm(forms.ModelForm):
    """
        A form that will allow the teacher to create a new
        course.
    """

    class Meta:
        """
            Associates this form with the Course model from the database
        """
        model = Course
        fields = ['class_name']

class CreateAttendanceForm(forms.Form):
    """
        A regular form that will help create a attendance session
    """

    # Will allow the teacher to pick how long the session should be
    duration_minutes = forms.IntegerField(
        label = "How many minutes should the attendance be active?",
        min_value = 1
    )
