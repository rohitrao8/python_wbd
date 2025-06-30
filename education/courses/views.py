from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course

class CourseListView(ListView):
    model = Course

class CourseDetailView(DetailView):
    model = Course

class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('course_list')
