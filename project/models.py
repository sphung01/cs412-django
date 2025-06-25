from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta


# Create your models here.
class ProjectUser(models.Model):
    """
        In the User model, we import from auth.models and add AbstractUser as
        a parameter. AbstractUser is useful because it provides a preset fields like
        'username', 'password', 'email', etc. It also keeps us from having to build from
        scratch. This is normal to use for when creating a account within a attendance system.
    """

    # We create roles so that whenever we make a dropdown list, it will have these options
    ROLES_TYPE = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )

    # These are the attributes/fields
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    email = models.CharField(max_length=250, blank=False)
    role = models.CharField(max_length=10, choices=ROLES_TYPE, blank=False) # Role of the User
    student_id = models.CharField(max_length=10, blank=True) # An ID if the student
    profile_image = models.ImageField(blank=True) # Optional if User wants to add pfp
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def is_student(self):
        """
            This method allows us to validate if the User is a student. This will
            prevent the student from entering views that only teachers should have
            access to.
        """
        if self.role == "Student":
            return True
        
    def is_teacher(self):
        """
            Same as the 'is_student' method. Will have access to nearly
            every view.
        """
        if self.role == "Teacher":
            return True
        
    def get_absolute_url(self):
        """
            Return the URL to display one instance of this model.
        """
        return reverse('project:account', kwargs={'pk':self.pk})
        
    def __str__(self):
        """
            Returns a string representation of the User object.
        """
        return f'Name: {self.first_name} {self.last_name} Role: {self.role}'
        
class Course(models.Model):
    """
        Represents a course model created by a User that has a role
        of a teacher.
    """

    # These are the attributes/fields
    # Course must be made by ProjectUser that is a teacher
    teacher = models.ForeignKey(ProjectUser, on_delete=models.CASCADE, limit_choices_to={'role':'Teacher'})

    # A generated code or identifier for the Course
    code = models.CharField(max_length=8, blank=False, unique=True) 
    
    # The name of the Course
    class_name = models.CharField(max_length=50, blank=False)

    # The time the Course was made
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
            Returns a string representation of the Course object.
        """
        return f'Course: {self.class_name} Created at: {self.created_at}'
    
class Enrollment(models.Model):
    """
        Represents a Enrollment model based on which course
        the student enrolled in.
    """

    # These are the attributes/fields

    # Only students should enroll
    student = models.ForeignKey(ProjectUser, on_delete=models.CASCADE, limit_choices_to={'role':'Student'})

    # Must be the specific Course they enrolled into
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    # The time they enrolled in the Course
    joined_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
            Returns a string representation of the Enrollment object.
        """

        return f'Name: {self.student.first_name} {self.student.last_name} - Enrolled: {self.course.class_name}'

class Attendance(models.Model):
    """
        Represents a Enrollment model based on which course
        the student enrolled in.
    """

    # These are the attributes/fields
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # The Course the attendance belongs to
    code = models.CharField(max_length=8, blank=False) # A random generated code for students to enter
    is_active = models.BooleanField(default=True) # To tell that the Attendance is active for students to prove their presence
    start_time = models.DateTimeField(default=timezone.now) # Start time of the code appearing
    end_time = models.DateTimeField() # And expiration time for the code

    def save(self, *args, **kwargs):
        # Set end_time to 2 mins after start_time if not already set

        # So if the expiration time does not exist,
        # then we can add 2 minutes to the start time
        if not self.end_time:
            self.end_time = self.start_time + timedelta(minutes=2)
        super().save(*args, **kwargs)

    def is_expired(self):
        """
            Now if we check that the time now is later than the expiration
            time, we return true that the session is over.
        """
        return timezone.now() > self.end_time

    def __str__(self):
        """
            Returns a string representation of the Attendance object.
        """
        return f'{self.course.class_name} - Active: {self.is_active}'

class Report(models.Model):
    """
        Represents a report of students record on attendance.
    """

    # These are the attributes/fields

    # Only students on this report
    student = models.ForeignKey(ProjectUser, on_delete=models.CASCADE, limit_choices_to={'role':'Student'})

    # A specific attendance taken in a Course
    attendance = models.ForeignKey(Attendance,on_delete=models.CASCADE)

    # The time the student was marked present
    time_marked = models.DateTimeField(auto_now=True)

    # If the student is present of absent
    status = models.CharField(max_length=8, blank=False)

    def __str__(self):
        """
            Returns a string representation of the Report object.
        """
        return f'{self.student.first_name} {self.student.last_name} - {self.status} Class: {self.attendance.course.class_name}'
