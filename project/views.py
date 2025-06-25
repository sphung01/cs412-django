from django.shortcuts import render
from .models import * 
from .forms import * 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, TemplateView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import string
import random
import time

# Create your views here.
def home(request):
    template = 'project/home.html'
    return render(request, template)

class CreateUserView(CreateView):
    """
        This view will display a form where the user will submit their
        account and it'll be saved to the database.   
        (1) display the HTML form to user (GET)
        (2) process the form submission and store the new Profile object (POST) 
    """

    # We will grab the CreateUserForm class from forms.py
    form_class = CreateUserForm

    # Then use a template where we will have the user sign up
    template_name = 'project/sign_up.html'

    # We also want to give the context by using UserCreationForm
    # so that we can make a username and password
    def get_context_data(self, **kwargs):
        """
            Within this method, we store values into the context and pass it
            over to the template.
        """
        context = super().get_context_data()
        context['user_creation_form'] = UserCreationForm() 
        return context
    

    def form_valid(self, form):
        '''
            This method handles the form submission and saves the 
            new object to the Django database.
        '''
        # Reconstruct the UserCreationForm instance 
        # from the self.request.POST data
        user_form = UserCreationForm(self.request.POST)

        if user_form.is_valid():
            # Call the save() method on the UserCreationForm instance. 
            # This method call will return the 
            # newly created User object. 
            # Save it to a variable.
            new_user = user_form.save()

            # Log the User in
            login(self.request, new_user)

            # Attach the new User to the ProjectUser being created
            form.instance.user = new_user

            # Delegate the work to the superclass method form_valid:
            return super().form_valid(form)
        else:
            # If the UserCreationForm is invalid, re-render the page with both forms
            return self.render_to_response(
                self.get_context_data(form=form, user_creation_form=user_form)
            )

class ShowAccountView(DetailView):
    """
        This view class will display the information about the user
    """
    model = ProjectUser
    template_name = 'project/show_my_account.html'
    context_object_name = 'account'

class ShowAllCoursesView(ListView):
    model = Course
    template_name = 'project/show_courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        # Only show courses created by the current teacher
        project_user = ProjectUser.objects.get(user=self.request.user)
        return Course.objects.filter(teacher=project_user)
    
class ShowAllEnrollmentsView(ListView):
    model = Enrollment
    template_name = 'project/show_enrollments.html'
    context_object_name = 'enrollments'

    def get_queryset(self):
        # Only show courses created by the current teacher
        project_user = ProjectUser.objects.get(user=self.request.user)
        return Enrollment.objects.filter(student=project_user)
    
class ShowCourseViewPage(DetailView):
    model = Course
    template_name = 'project/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attendances'] = self.object.attendance_set.order_by('-start_time')
        return context

class CreateCourseView(CreateView):
    form_class = CreateCourseForm
    template_name = 'project/create_course.html'

    def generate_unique_course_code(self):
        characters = string.ascii_uppercase + string.digits  # A-Z and 0-9
        while True:
            code = ''.join(random.choices(characters, k=6))
            if not Course.objects.filter(code=code).exists():
                return code

    def form_valid(self, form):
        teacher_profile = ProjectUser.objects.get(user=self.request.user)
        generated_code = self.generate_unique_course_code()

        # Inject missing fields into the unsaved form instance
        form.instance.teacher = teacher_profile
        form.instance.code = generated_code

        return super().form_valid(form)
    
class CreateEnrollmentView(CreateView):
    template_name = 'project/join_class_code.html'
    form_class = CreateEnrollmentForm

    def form_valid(self, form):

        code = self.request.POST.get('join_class_code')

        try:
            course = Course.objects.get(code=code)
            student_profile = ProjectUser.objects.get(user=self.request.user)
            if Enrollment.objects.filter(student=student_profile, course=course.pk).exists():
                form.add_error(None, "You are already enrolled in this course.")
                return self.form_invalid(form)
            new_enrollment = Enrollment(student=student_profile, course=course)
            new_enrollment.save()

        except Course.DoesNotExist:
            form.add_error('join_class_code', "No course found with this code.")
            return self.form_invalid(form)


        return super().form_valid(form)

class CreateReportView(CreateView):
    template_name = 'project/attendance_code.html'
    form_class = CreateReportForm

    def get_context_data(self, **kwargs):
        """
            Within this method, we store values into the context and pass it
            over to the template.
        """
        context = super().get_context_data()
        enrollment_id = self.kwargs['pk']
        enrollment = Enrollment.objects.get(pk=enrollment_id)
        context['enrollment'] = enrollment

        return context

    def form_valid(self, form):
        """
            This method handles the form submission and saves the 
            new object to the Django database.
            We need to add the foreign key (of the Profile) to the message
            object before saving it to the database.
        """

        # We get the code that the user submitted
        code = self.request.POST.get('attendance_code')
        print(self.request.POST)

        # Then we get that student object so that we know who did the attendance
        student_profile = ProjectUser.objects.get(user=self.request.user)

        # We will try to see if there is a attendance that matches the code entered
        try:
            # Search for the attendance object
            attendance = Attendance.objects.get(code=code)
            print(attendance)

            # Get the object of that student
            student_profile = ProjectUser.objects.get(user=self.request.user)

            # If the Report object happens to exist, we give an error.
            if Report.objects.filter(student=student_profile, attendance=attendance, status='Present').exists():
                return redirect(reverse('project:invalid_code', kwargs={'pk': self.kwargs['pk']}))
            
            # If it was successful and the attendance is active, then create a new report on that student
            if attendance.is_active == True:
                new_report = Report(student=student_profile, attendance=attendance, status='Present')
                new_report.save()
                return redirect(reverse('project:valid_code', kwargs={'pk': self.kwargs['pk']}))
            else:
                print('Here?')
                # Session is no longer active
                return redirect(reverse('project:invalid_code', kwargs={'pk': self.kwargs['pk']}))
        # If the object happens to not exist, that means the code was wrong
        except Attendance.DoesNotExist:
            return redirect(reverse('project:invalid_code', kwargs={'pk': self.kwargs['pk']}))


        # except Course.DoesNotExist:
        #     form.add_error('join_class_code', "No course found with this code.")
        #     return self.form_invalid(form)

class ShowValidCodePage(TemplateView):
    template_name = 'project/valid_code.html'

class ShowInvalidCodePage(TemplateView):
    template_name = 'project/invalid_code.html'

    def get_context_data(self, **kwargs):
        """
            Within this method, we store values into the context and pass it
            over to the template.
        """
        context = super().get_context_data()
        enrollment_id = self.kwargs['pk']
        enrollment = Enrollment.objects.get(pk=enrollment_id)
        context['enrollment'] = enrollment

        return context

    