# File: project/urls.py
# Author: Steven Phung (sphung01@bu.edu), 6/20/2025
# Description: This creates pathing to different pages
# within the project folder.

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import * #Adds all the view functions that exist
from django.contrib.auth import views as auth_views

"""
Configures URLs for the 'mini_fb' app

Routes:
- /project/ -> The home page of the website
- /project/login -> The login page for user to be authenticated
- /project/logout -> Logs the user out and redirects to home page
- /project/signup -> Allows the user to create new account
- /project/account/<int:pk> -> Displays account details of that user
- /project/courses/ -> Displays all courses the teacher has created
- /project/courses/create_course -> A page to create a new course
- /project/courses/course/<int:pk> -> A detail page of that course
- /project/courses/attendance/<int:pk> -> A page that displays the report of all students present of this attendance
- /project/courses/course/<int:pk>/attendance_session -> A page for the teacher to begin a session
- /project/courses/course/<int:pk>/delete -> A page to allow the teacher to delete the course
- /project/enrollments/ -> Displays all courses that the student is enrolled in
- /project/enrollments/join_class -> A form for a student to join a class
- /project/enrollments/take_attendance/<int:pk> -> Student enters a code to prove they are present in one of the classes
- /project/enrollments/take_attendance/<int:pk>/valid_code -> If the code is right, the student is present
- /project/enrollments/take_attendance/<int:pk>/invalid_code -> If the code is wrong, the student needs to retry


"static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"
This line serves all of the static files (CSS, Javascript, Images) to the project
during the deployment.
"""

# This 'app_name' is helpful and avoids user from
# navigating to a different app and built into Django's
# namespaced URL routing system. Due to both 'hw' and 'quotes'
# app that have same name of the HTML files, the user will accidentally
# go to another app. Common issue when using Django.
app_name = 'project'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='project/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='project:home'), name='logout'),
    path('signup/', CreateUserView.as_view(), name='sign_up'),
    path('account/<int:pk>', ShowAccountView.as_view(), name='account'),
    path('courses/', ShowAllCoursesView.as_view(), name='courses'),
    path('courses/create_course', CreateCourseView.as_view(), name='create_course'),
    path('courses/course/<int:pk>', ShowCourseViewPage.as_view(), name='course_detail'),
    path('courses/attendance/<int:pk>', ShowAttendanceReportPage.as_view(), name='attendance_report'),
    path('courses/course/<int:pk>/attendance_session', CreateAttendanceView.as_view(), name='attendance_session'),
    path('courses/course/<int:pk>/delete', DeleteCourseView.as_view(), name='delete_course'),
    path('enrollments/', ShowAllEnrollmentsView.as_view(), name='enrollments'),
    path('enrollments/join_class', CreateEnrollmentView.as_view(), name='join_class'),
    path('enrollments/take_attendance/<int:pk>', CreateReportView.as_view(), name='take_attendance'),
    path('enrollments/take_attendance/<int:pk>/valid_code', ShowValidCodePage.as_view(), name="valid_code"),
    path('enrollments/take_attendance/<int:pk>/invalid_code', ShowInvalidCodePage.as_view(), name="invalid_code"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)