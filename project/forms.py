from django import forms
from .models import *

class CreateUserForm(forms.ModelForm):
    """
        Adds a new user to the database
    """

    class Meta:
        """
            Associate this form with a model from our database.
        """
        model = ProjectUser
        fields = ['first_name', 'last_name', 'email', 'role', 'student_id', 'profile_image']

class CreateEnrollmentForm(forms.ModelForm):
    """
        Adds new enrollment instance to the database
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
        Adds new enrollment instance to the database
    """

    attendance_code = forms.CharField(label="Enter Code", max_length=6, required=True)

    class Meta:
        """
            Associates this form with the Enrollment model from the database
        """

        model = Report
        fields = ['attendance_code']

class CreateCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['class_name']