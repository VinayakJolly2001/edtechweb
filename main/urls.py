from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('aboutus/', views.about_us_view, name='about_us'),  # About Us
    path('courses/', views.courses_view, name='courses'),  # Courses
    path('form/', views.demo_form_view, name='demo_form'),
    path('form/', views.form_view, name='form'), 
]
